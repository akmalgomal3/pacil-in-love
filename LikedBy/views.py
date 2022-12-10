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
    SELECT username FROM "like"
    WHERE liked_user = '%s'
    ''' % (username))

    liked_by = fetch(cursor)
    likers_data = []
    for user in liked_by:
        
        print(user)

        current_user = user.get("username")
        cursor.execute(f'''
        SELECT * FROM profile
        WHERE username = '%s'
        ''' % current_user)
        user_data = fetch(cursor)

        print(user_data)
        print(type(user_data))
        kelamin = user_data[0].get("gender")
        if kelamin == "g001":
            user_data[0]["kelamin"] = "Laki-Laki"
        else:
            user_data[0]["kelamin"] = "Perempuan"
        likers_data.append(user_data)

    #DEBUG
    print(likers_data)
    #END DEBUG
    return render(request, 'view_liked_by.html', {'liked_by': likers_data})