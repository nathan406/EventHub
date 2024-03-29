from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class UserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email",'password1','password2')

class SignInForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username","password")