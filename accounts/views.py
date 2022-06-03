from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from accounts.forms import UserSignUpForm, MyLoginForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User


# class MyUserSignUpForm(UserSignUpForm):
#     # class Meta:
#     #     model = User
#     #     fields = [  "password1", "password2", "email", "username"]
#     #     help_texts = {
#     #         "password1":"",
#     #         "password2":"",
#     #         "email":"",
#     #         "username":"",}
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args,**kwargs)
#         # print(self.fields)
#         self.fields["password1"].help_text=""
#         self.fields["password2"].help_text=""
#         self.fields["email"].help_text=""
#         self.fields["username"].help_text=""


class UserCreationView(CreateView):
    form_class = UserSignUpForm
    success_url = reverse_lazy("login")  # Выполнить success_url когда будут прогружены все маршруты
    template_name = "accounts/sign_up.html"

    def get(self, request, *args, **kwargs):
        print("Сработал get ")
        if self.request.user.is_authenticated:
            return redirect("home")
        return super().get(request, *args, **kwargs)


class MyLoginView(LoginView):
    authentication_form = MyLoginForm

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("home")
        return super().get(request, *args, **kwargs)
