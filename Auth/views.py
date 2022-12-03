from django.http.response import JsonResponse, HttpResponse
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db import connection
from Auth.forms import loginForm, registerForm

# Create your views here.
def redirectLogin(request):return redirect('auth:login')


def loginPage(request):
    form = loginForm(request.POST or None)
    if (form.is_valid() and request.method == 'POST'):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        cursor = connection.cursor()

        cursor.execute("SET SEARCH_PATH TO public")
        cursor.execute("SELECT * FROM pengguna where username ='"+username+"' and password = '"+password +"'")
        result = cursor.fetchone()
        print(result)

        if result == None:
            return HttpResponseNotFound("The user does not exist")

        cursor.execute("SELECT * FROM profile where username ='"+username+"'")
        result = cursor.fetchone()
        
        role = result[5]
        print(role)


        cursor.execute("SET SEARCH_PATH TO public")
        request.session['username'] = username
        if role == 'r001':
            request.session['role'] = 'admin'
        else:
            request.session['role'] = 'user'

        return redirect('home:homepage')


    return render(request, 'loginpage.html', {'form' : form})

def registerPage(request):
    form = registerForm(request.POST or None)
    if (form.is_valid() and request.method == 'POST'):
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']

        cursor = connection.cursor()

        cursor.execute("SET SEARCH_PATH TO public")
        cursor.execute("SELECT * FROM pengguna where username ='"+username+"'")
        result = cursor.fetchone()

        if (result == None):
            cursor.execute("SET SEARCH_PATH TO public")
            cursor.execute("INSERT INTO pengguna (username, password) VALUES('"+username+"','"+password+"')")
            cursor.execute("INSERT INTO profile (username, email, role) VALUES('"+username+"','"+email+"', 'r002')")

            cursor.execute("select max(id_username) from list_username")
            max_id = cursor.fetchone()[0]
            max_id += 1
            cursor.execute("INSERT INTO list_username (id_username, username) VALUES('"+str(max_id)+"','"+username+"')")

            return HttpResponseRedirect('/homepage')
        
        else:
            return HttpResponseNotFound("The user already exist")

    return render(request, 'registerpage.html', {'form' : form})
    
def logout(request):
   try:
        del request.session['username']
        del request.session['role']
   except:
        pass
   return redirect('auth:login')
