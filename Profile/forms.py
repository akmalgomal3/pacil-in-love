import imp
from django import forms
from django.forms import Form
from django.db import connection

gender = [
    ('laki-laki', 'Laki-laki'),
    ('perempuan', 'Perempuan'),
]


class createProfileForm(forms.Form):
    name = forms.CharField(label='Nama Lengkap', max_length=50)
    gender = forms.CharField(label='Jenis Kelamin', widget=forms.Select(choices=gender))
    phone = forms.CharField(label='Phone Number', max_length=50)
    umur = forms.IntegerField(label='Umur')


class updateProfileForm(forms.Form):
    name = forms.CharField(label='Nama Lengkap', max_length=50)
    gender = forms.CharField(label='Jenis Kelamin', widget=forms.Select(choices=gender))
    phone = forms.CharField(label='Phone Number', max_length=50)
    umur = forms.IntegerField(label='Umur')

class updateUsernamePassword(forms.Form):
    username = forms.CharField(label='Username', max_length=50)
    password = forms.CharField(label='Password', max_length=50, widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Confirm Password', max_length=50, widget=forms.PasswordInput)