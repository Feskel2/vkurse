from django import forms
# from .models import User
from django.contrib.auth.forms import AuthenticationForm

class AuthUserForm (AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
