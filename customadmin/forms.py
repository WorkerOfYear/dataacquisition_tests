from django import forms
from django.core.exceptions import ValidationError

from .models import CustomUser, Item


class LoginForm(forms.Form):
    """
    Форма для входа в аккаунт
    """

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    """
    Форма для создания user
    """

    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat password", widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ["username"]

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password and password2 and password != password2:
            raise ValidationError("Passwords don't match")
        return password2


class UserForm(forms.ModelForm):
    """
    Форма для редактированя user
    """

    class Meta:
        model = CustomUser
        fields = ("username",)


class ItemForm(forms.ModelForm):
    """
    Форма для создания и редактирования item
    """

    class Meta:
        model = Item
        # fields = ("name", "user_id")
        fields = "__all__"
