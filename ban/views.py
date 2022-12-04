from django.http.response import JsonResponse, HttpResponse
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db import connection
from Auth.views import *
from Auth.urls import *
import datetime

def banPage(request):
    userUsername = checkLoggedIn(request)
    
    if not userUsername:
        return redirect('auth:login')

    cursor = connection.cursor()

    cursor.execute("SET SEARCH_PATH TO public")
    cursor.execute("SELECT * FROM reported_user")

    list = {}
    list = cursor.fetchall()

    if request.session['role'] == 'user':
        return redirect('home:homepage')
    
    return render(request, 'banpage.html', {'list': list})

def req_timeout(request, username):
    if request.method == "GET":
        print('Tombol timeout dipencet')
        print(username)

        current_datetime = datetime.datetime.now()
        print(current_datetime)

        cursor = connection.cursor()

        cursor.execute("SET SEARCH_PATH TO public")
        cursor.execute("UPDATE pengguna SET timeout = '"+str(current_datetime)+"' WHERE username='"+username+"'")

    return HttpResponseRedirect('/ban')

def req_delete(request, username):
    if request.method == "GET":
        print('Tombol delete dipencet')
        print(username)

        cursor = connection.cursor()

        cursor.execute("SET SEARCH_PATH TO public")
        cursor.execute("DELETE FROM pengguna WHERE username='"+username+"'")

    return HttpResponseRedirect('/ban')