from django.http.response import JsonResponse, HttpResponse
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db import connection
from Profile.forms import createProfileForm, updateProfileForm, updateUsernamePassword

def profile(request):
    if request.session.has_key('username'):
        username = request.session['username'][0]
        cursor = connection.cursor()

        cursor.execute("SET SEARCH_PATH TO public")
        cursor.execute("SELECT * from profile where username = '"+username+"'")
        profile = cursor.fetchone()
        return render(request, 'profilePage.html', {'profile' : profile})
    else:
        return redirect('auth:login')
        

def createProfilePage(request):
    form = createProfileForm(request.POST or None)
    if request.session.has_key('username'):
        username = request.session['username'][0]
        if (form.is_valid() and request.method == 'POST'):
            name = form.cleaned_data['name']
            gender = form.cleaned_data['gender']
            phone = form.cleaned_data['phone']
            umur = form.cleaned_data['umur']

            cursor = connection.cursor()

            cursor.execute("SET SEARCH_PATH TO public")
            
            if gender == 'laki-laki':
                gender = 'g001'
            else:
                gender = 'g002'

            cursor.execute("INSERT INTO profile (gender, Phone, name_lengkap, umur) VALUES('"+gender+"','"+phone+"', '"+name+"', '"+umur+"') where username = '"+username+"'")
            
            return redirect('home:homepage')
    else:
        return redirect('auth:login')
    return render(request, 'createProfilePage.html', {'form' : form})

def updateProfilePage(request):
    form = updateProfileForm(request.POST or None)
    if request.session.has_key('username'):
        username = request.session['username'][0]
        if (form.is_valid() and request.method == 'POST'):
            name = form.cleaned_data['name']
            gender = form.cleaned_data['gender']
            phone = form.cleaned_data['phone']
            umur = form.cleaned_data['umur']

            cursor = connection.cursor()

            cursor.execute("SET SEARCH_PATH TO public")
            
            if gender == 'laki-laki':
                gender = 'g001'
            else:
                gender = 'g002'

            cursor.execute("update profile set gender = '"+gender+"', phone = '"+phone+"', nama_lengkap = '"+name+"', umur = '"+umur+"' where username = '"+username+"'")
            
            return redirect('home:homepage')
    else:
        return redirect('auth:login')
    return render(request, 'updateProfilePage.html', {'form' : form})

def updateUsernamePasswordPage(request):
    form = updateUsernamePassword(request.POST or None)
    if request.session.has_key('username'):
        username = request.session['username'][0]
        if (form.is_valid() and request.method == 'POST'):
            username_new = form.cleaned_data['username']
            password_new = form.cleaned_data['password']

            cursor = connection.cursor()

            cursor.execute("SET SEARCH_PATH TO public")
            cursor.execute("select * from pengguna")
            list_pengguna = cursor.fetchall()

            if username_new in list_pengguna:
                HttpResponseNotFound('Username sudah dilimiki.')
            elif form.cleaned_data['password']==form.cleaned_data['password_2']:
                HttpResponseNotFound('Confirm password salah')
            
            cursor.execute("update pengguna set username = '"+username_new+"'and password = '"+password_new+"'where username = '"+username+"'")
            return redirect('home:homepage')
        
    else:
        return redirect('auth:login')
    return render (request, 'updateUsernamePasswordPage.html', {'form':form})