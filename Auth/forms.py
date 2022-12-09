import imp
from django import forms
from django.forms import Form

class loginForm(forms.Form):
    username = forms.CharField(label='username', max_length=50, widget=forms.TextInput(attrs=({'placeholder': 'username', 'style': 'width: 300px;', 'class': 'form-control'})))
    password = forms.CharField(label='password', max_length=50, widget=forms.PasswordInput(attrs=({'placeholder': 'password', 'style': 'width: 300px;', 'class': 'form-control'})))

class registerForm(forms.Form):
    username = forms.CharField(label='Username', max_length=50, widget=forms.TextInput(attrs=({'placeholder': 'username', 'style': 'width: 300px;', 'class': 'form-control'})))
    email = forms.CharField(label='E-Mail Address', max_length=50, widget=forms.TextInput(attrs=({'placeholder': 'e-mail', 'style': 'width: 300px;', 'class': 'form-control'})))
    password = forms.CharField(label='Password', max_length=50, widget=forms.PasswordInput(attrs=({'placeholder': 'password', 'style': 'width: 300px;', 'class': 'form-control'})))