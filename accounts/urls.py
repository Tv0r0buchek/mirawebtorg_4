from django.urls import path
import django.contrib.auth.views as auth_views
from accounts.views import UserCreationView, MyLoginView, MyPasswordResetView


urlpatterns = [
    path("login/", MyLoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("signUp/", UserCreationView.as_view(), name="signUp"),

    path("changePassword/", auth_views.PasswordChangeView.as_view(), name="change_password"),
    path("passwordChangeDone/", auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),

    path("password_reset/", MyPasswordResetView.as_view(
        template_name="registration/my_password_reset_form.html"
    ), name="password_reset"),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(
        template_name="registration/password_reset_done_form.html"), name="password_reset_done"),
    path("password_reset_confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(
        template_name="registration/password_reset_confirm_form.html"), name="password_reset_confirm"),
    path("password_reset/complete/", auth_views.PasswordResetCompleteView.as_view(
        template_name="registration/my_password_reset_complete.html"
    ))
]
