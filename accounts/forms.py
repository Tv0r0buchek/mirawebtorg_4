from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from core.models import Review


# class UserSignUpForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#     class Meta:
#         model = User
#         fields = ["username", "email", "password1","password2"]



class UserSignUpForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "area", "placeholder": "Никнейм"}),
        label="")

    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "area", "placeholder": "Ваше имя"}),
        label="")

    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "area", "placeholder": "Ваша фамилия"}),
        label="")

    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={"class": "area", "placeholder": "Придумайте пароль"}), label="")

    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={"class": "area", "placeholder": "Подтвердите пароль"}), label="")

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={"class": "area", "placeholder": "Ваш Email"}), label="")


    class Meta:
        model = User
        fields = ["username","first_name","last_name", "email", "password1", "password2"]



class MyLoginForm(AuthenticationForm):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "area","placeholder":"Введите никнейм"}),
        label="")
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={"class": "area", "placeholder": "Введите пароль"}), label="")