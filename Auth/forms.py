import imp
from django import forms
from django.forms import Form

class loginForm(forms.Form):
    username = forms.CharField(label='E-Mail Address', max_length=50)
    password = forms.CharField(label='Password', max_length=50, widget=forms.PasswordInput)

class registerForm(forms.Form):
    username = forms.CharField(label='Username', max_length=50)
    email = forms.CharField(label='E-Mail Address', max_length=50)
    password = forms.CharField(label='Password', max_length=50, widget=forms.PasswordInput)