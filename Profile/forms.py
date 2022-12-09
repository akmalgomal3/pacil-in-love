import imp
from django import forms
from django.forms import Form
from django.db import connection

gender = [
    ('laki-laki', 'Laki-laki'),
    ('perempuan', 'Perempuan'),
]
cursor = connection.cursor()

cursor.execute("SET SEARCH_PATH TO public")
cursor.execute("SELECT * from list_hobi")
hobi = cursor.fetchall()

list_hobi = []
for i in hobi:
    list_hobi.append((i[0], i[1]))

list_hobi = tuple(list_hobi)

class createProfileForm(forms.Form):
    name = forms.CharField(label='Nama Lengkap', max_length=50, widget=forms.TextInput(attrs=({'placeholder': 'Name', 'style': 'width: 300px;', 'class': 'form-control'})))
    gender = forms.CharField(label='Jenis Kelamin', widget=forms.Select(choices=gender, attrs=({'style': 'width: 300px;', 'class': 'form-control'})))
    phone = forms.CharField(label='Phone Number', max_length=50, widget=forms.TextInput(attrs=({'placeholder': 'Number', 'style': 'width: 300px;', 'class': 'form-control'})))
    umur = forms.IntegerField(label='Umur', widget=forms.NumberInput(attrs=({'placeholder': 'Age', 'style': 'width: 300px;', 'class': 'form-control'})))
    image = forms.URLField()
    hobby = forms.MultipleChoiceField(widget = forms.CheckboxSelectMultiple,choices=list_hobi)

class updateProfileForm(forms.Form):
    name = forms.CharField(label='Nama Lengkap', max_length=50, widget=forms.TextInput(attrs=({'placeholder': 'Name', 'style': 'width: 300px;', 'class': 'form-control'})))
    gender = forms.CharField(label='Jenis Kelamin', widget=forms.Select(choices=gender, attrs=({'style': 'width: 300px;', 'class': 'form-control'})))
    phone = forms.CharField(label='Phone Number', max_length=50, widget=forms.TextInput(attrs=({'placeholder': 'Number', 'style': 'width: 300px;', 'class': 'form-control'})))
    umur = forms.IntegerField(label='Umur', widget=forms.NumberInput(attrs=({'placeholder': 'Age', 'style': 'width: 300px;', 'class': 'form-control'})))
    image = forms.URLField()
    hobby = forms.MultipleChoiceField(widget = forms.CheckboxSelectMultiple,choices=list_hobi)

class updatePassword(forms.Form):
    old_password = forms.CharField(label='Old Password', max_length=50, widget=forms.PasswordInput(attrs=({'placeholder': 'old password', 'style': 'width: 300px;', 'class': 'form-control'})))
    new_password = forms.CharField(label='New Password', max_length=50, widget=forms.PasswordInput(attrs=({'placeholder': 'new password', 'style': 'width: 300px;', 'class': 'form-control', 'name':'new_password'})))
    confirm_password = forms.CharField(label='Confirm Password', max_length=50, widget=forms.PasswordInput(attrs=({'placeholder': 'confirm password', 'style': 'width: 300px;', 'class': 'form-control', 'name':'comfirm_password'})))