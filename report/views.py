from django.shortcuts import render
from Auth.views import *
from Auth.urls import *
from django.shortcuts import *
import django.db as db
from django.db import connection
from Home import *

# Create your views here.
def report(request):
    userUsername = checkLoggedIn(request)
    
    if not userUsername:
        return redirect('auth:login')

    # username = data[username]
    # reason = data[reason]
    if request.method == 'POST':
        username = "bintangns"
        reason = "rr001"

        # username = data['username']
        # reason = data['reason']
        
        isValid = 0;


        try:
            cursor = connection.cursor()
            cursor.execute("set search_path to public")

            cursor.execute("INSERT INTO REPORTED_USER VALUES (%s, %s)", [username, reason])

        except db.Error as e:
            message = e
            isValid += 1
    return redirect('home:homepage')

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

        


        

