from django import forms
from .models import CustomUser, Item


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("username",)


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        # fields = ("name", "user_id")
        fields = "__all__"


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat password", widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ["username"]

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Passwords don't match.")
        return cd["password2"]
