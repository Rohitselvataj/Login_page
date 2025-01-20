from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, AdminUpdate

class CustomUser(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'is_admin', 'is_user']

class AdminUpdateForm(forms.ModelForm):
    class Meta:
        model = AdminUpdate
        fields = ['title', 'description']

class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']