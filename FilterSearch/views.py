from django.shortcuts import render
from django.shortcuts import render
from Auth.views import *
from Auth.urls import *
from django.shortcuts import *
import django.db as db
from django.db import connection
from Home import *

# Create your views here.


def filterbyhobi(request):
    userUsername = checkLoggedIn(request)

    if not userUsername:
            return redirect('auth:login')

    cursor = connection.cursor()
    cursor.execute("set search_path to public")
    data = request.POST
    list_user = {}
    response = {}

    pesan = "Tidak ada user dengan hobi ini"

    if request.method ==- 'POST':
        hobi = data['hobi']

        try:
            cursor.execute("set search_path to public")
            cursor.execute(
                "SELECT * FROM list_username right join selected_hobi sh on list_username.username = sh.username WHERE hobi = %s", [hobi]
            )
            list_user = cursor.fetchall()

            return render(request, 'temp.html', {'list_user': list_user})
        except Exception:
            e = 'Tidak ada user dengan hobi ini'
            response['message'] = e
            
    return render(request, 'temp.html', response)



        