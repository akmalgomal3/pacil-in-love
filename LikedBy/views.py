from django.db import connection
from django.shortcuts import redirect, render
from random import randrange

# Create your views here.
def fetch(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def get_list_liked_by(request):
    cursor = connection.cursor()
    cursor.execute("SET search_path TO public")
    
    username = request.session['username']
    cursor.execute(f'''
    SELECT username FROM LIKE
    WHERE liked_user = '%s'
    ''' % (username))

    liked_by = cursor.fetchall()
    return liked_by