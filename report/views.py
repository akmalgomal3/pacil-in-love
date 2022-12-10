from django.shortcuts import render
from Auth.views import *
from Auth.urls import *
from django.shortcuts import *
import django.db as db
from django.db import connection
from Home import *
from Profile import *

# Create your views here.
def report(request, pengguna):
    userUsername = checkLoggedIn(request)
    response = {}
    if not userUsername:
        return redirect('auth:login')

    if request.session['role'] == 'user':
        cursor = connection.cursor()
        cursor.execute("set search_path to public")

        cursor.execute("SELECT username FROM pengguna where username = %s", [pengguna])
        nama_pengguna = cursor.fetchall()
        response['nama_pengguna'] = nama_pengguna

        cursor.execute("SELECT nama_lengkap FROM profile where username = %s", [pengguna])
        nama_lengkap = cursor.fetchall()
        response['nama_lengkap'] = nama_lengkap

        kode = "rr%"

        cursor.execute("SELECT id_reason from reported_reason where id_reason like %s", [kode])
        idReason = cursor.fetchall()
        response['idReason'] = idReason

        if request.method == 'POST':
            data = request.POST
            id_Reason = data['idReason']
            nama = pengguna

            cursor.execute("INSERT INTO REPORTED_USER VALUES (%s, %s)", [nama, id_Reason])

            return redirect('/profile')

        return render(request, 'report.html', response)


def list_reported(request):
    userUsername = checkLoggedIn(request)
    reported_user = {}

    if not userUsername:
        return redirect('auth:login')

    if request.session['role'] == 'admin':
        cursor = connection.cursor()
        cursor.execute("SET search_path to public")
        
        cursor.execute("SELECT * FROM reported_user")
    
        reported_user = cursor.fetchall()

        return render(request, 'reported_user.html', {'reported_user' : reported_user})

    else:
        return redirect('home:homepage')

        


        

