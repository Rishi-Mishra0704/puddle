from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Your username', 'class': 'w-full px-4 py-6 rounded-xl'})
    )

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Your email', 'class': 'w-full px-4 py-6 rounded-xl'})
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Your password', 'class': 'w-full px-4 py-6 rounded-xl'})
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Confirm your password', 'class': 'w-full px-4 py-6 rounded-xl'})
    )