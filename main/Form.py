from django import forms
from django.contrib.auth.models import User
from .models import Data


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', "email"]


class MediaForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['data_type', 'data_file', 'data_name']
