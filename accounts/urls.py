from django.urls import path
import django.contrib.auth.views as auth_views
from accounts.views import UserCreationView, MyLoginView


urlpatterns = [
    path("login/",MyLoginView.as_view(), name="login"),
    path("logout/",auth_views.LogoutView.as_view(), name="logout"),
    path("signUp/",UserCreationView.as_view(),name="signUp"),
    path("changePassword/", auth_views.PasswordChangeView.as_view(), name="changePassword"),
    path("passwordChangeDone", auth_views.PasswordChangeDoneView.as_view(), name="passwordChangeDone")
]