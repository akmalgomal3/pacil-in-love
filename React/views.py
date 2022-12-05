from django.db import connection
from django.shortcuts import redirect, render
from random import randrange

def fetch(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


# Create your views here.
def index(request):

    cursor = connection.cursor()
    cursor.execute("set search_path to public")

    username = request.session['username']
    role = request.session['role']

    cursor.execute(f'''
                    select id_username 
                    from list_username
                    where username != '%s' and id != 1
                    order by random()
                    limit 1
                    ''' % (username))

    user = cursor.fetchone()
    if user != '':
        cursor.execute(f'''
            select *
            from profile
            where username = '%s'
                ''' % (user))

        data_user = fetch(cursor)

    return render(request, 'react_home.html', {'data' : data_user})
    
def like(request):

    cursor = connection.cursor()
    cursor.execute("set search_path to public")
    
    username = request.session['username']
    role = request.session['role']

    cursor.execute(f'''
        select liked_user
        from "like"
        where username = '%s'    
    ''' % (username))
    
    liked_user = cursor.fetchall()

    if request.method == 'POST':
        data = request.POST
        nama = data['user']

        print(nama)
        if nama != '':
            if nama not in liked_user:
                cursor.execute(f'''
                    insert into "like" values ('%s', '%s')
                ''' % (username, nama))

            cursor.execute(f'''
                select liked_user
                from "like"
                where username = '%s'    
            ''' % (nama))

            list_liked = cursor.fetchall()

            if username in list_liked:
                return render(request)

    return render(request)

def dislike(request):
    cursor = connection.cursor()
    cursor.execute("set search_path to public")
    
    username = request.session['username']
    role = request.session['role']
    
    if request.method == "POST":
        data = request.POST
        nama = data['user']

        return redirect('home:homepage')
    
    return render(request)