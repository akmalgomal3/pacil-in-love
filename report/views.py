from django.shortcuts import render
from Auth.views import *
from Auth.urls import *
from django.shortcuts import *
import django.db as db
from django.db import connection

# Create your views here.
def report(request):
    userUsername = checkLoggedIn(request)
    
    if not userUsername:
        return redirect('auth:login')

    # username = data[username]
    # reason = data[reason]
    if request.method == 'POST':
        username = "bintangns"
        reason = "Sampah"

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
    return render(request, 'home.html', {'message': message})

def list_reported(request):
    userUsername = checkLoggedIn(request)

    if not userUsername:
        return redirect('auth:login')

    if request.session['admin']:
        cursor = connection.cursor()
        cursor.execute("SET search_path to public")
        
        cursor.execute("SELECT * FROM reported_user")

    else:
        return redirect('Home:homepage')

        


        

