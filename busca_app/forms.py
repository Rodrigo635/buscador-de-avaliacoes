from django import forms
from django.contrib.auth.models import User, Group
from .models import *

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = '__all__'