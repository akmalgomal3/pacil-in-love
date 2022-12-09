from django.http.response import JsonResponse, HttpResponse
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db import connection
from Profile.forms import createProfileForm, updateProfileForm, updatePassword
from django.contrib import messages

def profile(request):
    if request.session.has_key('username'):
        username = request.session['username']
        cursor = connection.cursor()

        cursor.execute("SET SEARCH_PATH TO public")
        cursor.execute("SELECT * from profile where username = '"+username+"'")
        temp = cursor.fetchone()
        cursor.close()
        gender = ""
        if temp[2] == 'g001':
            gender = 'Laki-laki'
        elif temp[2] == 'g002':
            gender = 'Perempuan'

        profile = {"name":temp[4],
                    "username":temp[0],
                    "email":temp[1],
                    "jenis_kelamin":gender,
                    "nomor":temp[3],
                    "umur":temp[6]}



        return render(request, 'profilePage.html', profile)
    else:
        return redirect('auth:login')
        

def createProfilePage(request):
    form = createProfileForm(request.POST, request.FILES)
    if request.session.has_key('username'):
        username = request.session['username']
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

            cursor.execute("update profile set gender = '"+gender+"', phone = '"+phone+"', nama_lengkap = '"+name+"', umur = '"+str(umur)+"' where username = '"+username+"'")
            
            return redirect('home:homepage')
    else:
        return redirect('auth:login')
    return render(request, 'createProfilePage.html', {'form' : form})

def updateProfilePage(request):
    form = updateProfileForm(request.POST or None)
    if request.session.has_key('username'):
        username = request.session['username']
        if (form.is_valid() and request.method == 'POST'):
            name = form.cleaned_data['name']
            gender = form.cleaned_data['gender']
            phone = form.cleaned_data['phone']
            umur = form.cleaned_data['umur']
            image = form.cleaned_data['image']

            print(image)

            cursor = connection.cursor()

            cursor.execute("SET SEARCH_PATH TO public")
            
            if gender == 'laki-laki':
                gender = 'g001'
            else:
                gender = 'g002'

            cursor.execute("update profile set gender = '"+gender+"', phone = '"+phone+"', nama_lengkap = '"+name+"', umur = '"+str(umur)+"', picture = '"+image+"' where username = '"+username+"'")
            messages.success(request, "Profile Updated.")
            return redirect('profile:profile')
    else:
        return redirect('auth:login')
    return render(request, 'updateProfilePage.html', {'form' : form})

def updatePasswordPage(request):
    form = updatePassword(request.POST or None)
    if request.session.has_key('username'):
        username = request.session['username']
        if (form.is_valid() and request.method == 'POST'):
            old_password = form.cleaned_data['old_password']
            password_new = form.cleaned_data['new_password']

            cursor = connection.cursor()

            cursor.execute("SET SEARCH_PATH TO public")
            cursor.execute("select password from pengguna where username = '"+username+"'")
            password = cursor.fetchone()[0]
            print(password)

            if old_password != password:
                messages.error(request, "Old Password and Current Password didn't match")
                return redirect('profile:update_auth')
            elif form.cleaned_data['new_password']!=form.cleaned_data['confirm_password']:
                messages.error(request, "New Password and Confirm Password didn't match")
                return redirect('profile:update_auth')
            else:
                messages.success(request, "Password Updated.")
                cursor.execute("update pengguna set password = '"+password_new+"'where username = '"+username+"'")
                return redirect('profile:profile')

    else:
        return redirect('auth:login')
    return render (request, 'updatePasswordPage.html', {'form':form})