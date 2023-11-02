from django.urls import reverse_lazy, reverse
from django.views.generic import DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, UserRegistrationForm, ItemForm, UserForm
from .models import CustomUser, Item


home_url = "customadmin:dashboard"


def edit_object(request, id, object_type):
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


def delete_object(request, id, object_type):
    if object_type == "CustomUser":
        obj = get_object_or_404(CustomUser, id=id)
        obj.delete()
    elif object_type == "Item":
        obj = get_object_or_404(Item, id=id)
        obj.delete()
    return redirect(home_url)


def create_item(request):
    if request.method == "POST":
        item_form = ItemForm(request.POST)
        if item_form.is_valid():
            item_form.save()
            return redirect(home_url)
    else:
        item_form = ItemForm()
    return render(request, "customadmin/create_item.html", {"item_form": item_form})


def create_user(request):
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


def dashboard(request):
    if request.method == "POST":
        user_selected_fields = request.POST.getlist("user_selected_fields")
        item_selected_fields = request.POST.getlist("item_selected_fields")
    else:
        user_selected_fields = None
        item_selected_fields = None

    user_white_list = ["username"]
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

    users = CustomUser.objects.all()  # можно добавить select_related
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
