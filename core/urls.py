from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("contact/", views.contact, name="contact"),
    path("signup/", views.signup, name="signup"),
    path("login/", auth_views.LoginView.as_view(template_name="core/login.html",authentication_form=LoginForm), name="login"),
] 