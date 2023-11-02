from django.urls import reverse_lazy, reverse
from django.views.generic import DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, UserRegistrationForm, ItemForm, UserForm
from .models import CustomUser, Item


home_url = "customadmin:dashboard"


@login_required
def edit_object(request, id, object_type):
    """
    Представлене для редактирования объекта модели

    id: int - идентификатор объекта
    object_type: str - название модели в которой редактируется объект

    """

    if object_type == "Item":
        item = get_object_or_404(Item, id=id)
        if request.method == "POST":
            form = ItemForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                return redirect(home_url)
        else:
            form = ItemForm(instance=item)
        return render(request, "customadmin/edit.html", {"form": form})

    if object_type == "CustomUser":
        user = get_object_or_404(CustomUser, id=id)
        if request.method == "POST":
            form = UserForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                return redirect(home_url)
        else:
            form = UserForm(instance=user)
        return render(request, "customadmin/edit.html", {"form": form})

    return redirect(home_url)


@login_required
def delete_object(request, id, object_type):
    """
    Представление для удаления обекта модели

    id: int - идентификатор объекта
    object_type: str - название модели в которой удаляется объект

    """
    if object_type == "CustomUser":
        obj = get_object_or_404(CustomUser, id=id)
        obj.delete()
    elif object_type == "Item":
        obj = get_object_or_404(Item, id=id)
        obj.delete()
    return redirect(home_url)


@login_required
def create_item(request):
    """
    Представление для создания обекта модели Item

    """

    if request.method == "POST":
        item_form = ItemForm(request.POST)
        if item_form.is_valid():
            item_form.save()
            return redirect(home_url)
    else:
        item_form = ItemForm()
    return render(request, "customadmin/create_item.html", {"item_form": item_form})


@login_required
def create_user(request):
    """
    Представление для создания обекта модели User

    """

    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()
            return redirect(home_url)
    else:
        user_form = UserRegistrationForm()
    return render(request, "customadmin/create_user.html", {"user_form": user_form})


@login_required
def dashboard(request):
    """
    Представление для рендеринга дашборда с таблицами Users и Items

    user_selected_fields и item_selected_fields -
    """

    if request.method == "POST":
        # получаем выбранные пользователям поля в фильтре отображения
        user_selected_fields = request.POST.getlist("user_selected_fields")
        item_selected_fields = request.POST.getlist("item_selected_fields")
    else:
        user_selected_fields = None
        item_selected_fields = None

    # Так как модель CustomUser наследуется от модели AbstractUser,
    # то создаются поля, которые мы не хотим отображать.
    # поэтому мы включаем все поля от AbstractUser в user_black_list,
    # поля которые мы хотим видить от AbstractUser в user_white_list

    user_white_list = ["username", "is_superuser"]
    user_black_list = ["logentry", "item"]
    abstractuser_fields = AbstractUser._meta.get_fields()
    abstractuser_fields = list(map(lambda field: field.name, abstractuser_fields))
    user_black_list += abstractuser_fields

    user_allfields = CustomUser._meta.get_fields()
    user_allfields = list(map(lambda field: field.name, user_allfields))
    user_fields = []
    for field in user_allfields:
        if field not in user_black_list or field in user_white_list:
            user_fields.append(field)
    user_allfields = user_fields

    if user_selected_fields:
        user_fields = user_selected_fields

    item_fields = Item._meta.get_fields()
    item_allfields = list(map(lambda field: field.name, item_fields))
    if item_selected_fields:
        item_fields = item_selected_fields
    else:
        item_fields = item_allfields

    users = CustomUser.objects.all()
    items = Item.objects.all()

    return render(
        request,
        "customadmin/dashboard.html",
        {
            "user_allfields": user_allfields,
            "item_allfields": item_allfields,
            "user_fields": user_fields,
            "item_fields": item_fields,
            "users": users,
            "items": items,
        },
    )
