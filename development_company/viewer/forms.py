from django import forms

import re
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя',widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Пароль',widget=forms.PasswordInput(attrs={'class':'form-control'}))