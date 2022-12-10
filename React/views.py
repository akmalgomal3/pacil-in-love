from django.db import connection
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from Auth.views import checkLoggedIn


def fetch(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


# Create your views here.
def index(request):
    if not checkLoggedIn(request):
        return redirect('auth:login')

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
    print(liked_user)

    cursor.execute(f'''
                    select username
                    from list_username
                    where username != '%s' and id_username != 1
                    order by random()
                    ''' % (username))

    user_list = cursor.fetchall()
    print(user_list)
    for i in user_list:
        if i not in liked_user:
            user = i
            break

    print(user)
    cursor.execute(f'''
        select *
        from profile p full join gender g on p.gender = g.id_gender
        where username = '%s'
            ''' % (user))

    data_user = fetch(cursor)
    print(data_user)

    cursor.execute("select * from list_hobi")
    idHobi = fetch(cursor)

    cursor.execute(f'''
        select *
        from selected_hobi sh left join list_hobi lh on sh.hobi = lh.id_hobi
        where username = '%s'
            ''' % (user))
    hobies = fetch(cursor)

    list_hobi = []
    for hobi in hobies:
        list_hobi.append(hobi['nama_hobi'])
    print(list_hobi)

    return render(request, 'react_home.html', {'data' : data_user, 'hobi' : list_hobi, 'idsHobby' : idHobi, 'selected_hobi' : None})

def filterHobby(request, hobbyID):
    if not checkLoggedIn(request):
        return redirect('auth:login')

    cursor = connection.cursor()
    cursor.execute("set search_path to public")

    username = request.session['username']
    cursor.execute("select * from list_hobi")
    idHobi = fetch(cursor)
    print(hobbyID)
    cursor.execute(f'''
    select liked_user
    from "like"
    where username = '%s'    
    ''' % (username))

    liked_user = cursor.fetchall()

    cursor.execute(f'''
                select list_username.username
                from list_username right join selected_hobi sh on list_username.username = sh.username
                where list_username.username != '%s' and list_username.id_username != 1 and hobi = '%s'
                order by random()
                ''' % (username, hobbyID))

    user_list = cursor.fetchall()
    print(user_list)
    user = None
    for i in user_list:
        if i not in liked_user:
            user = i
            break  
    if user == None:
        return redirect('react:index')
    print(user)
    cursor.execute(f'''
        select *
        from profile p full join gender g on p.gender = g.id_gender
        where username = '%s'
            ''' % (user))

    data_user = fetch(cursor)
    
    cursor.execute(f'''
        select *
        from selected_hobi sh left join list_hobi lh on sh.hobi = lh.id_hobi
        where username = '%s'
            ''' % (user))
    hobies = fetch(cursor)

    list_hobi = []
    for hobi in hobies:
        list_hobi.append(hobi['nama_hobi'])
    print(list_hobi)
    
    print(data_user)
    print(hobbyID)
    return render(request, 'react_home.html', {'data' : data_user, 'hobi' : list_hobi, 'idsHobby': idHobi, 'selected_hobi':hobbyID})


    
def like(request, user, id_hobi):

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

    nama = user

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
            return redirect('react:match')

    return redirect('/react/' + id_hobi)

def dislike(request, id_hobi):
    return redirect('/react/' + id_hobi)

def match(request):
    return render(request, 'match.html', {'selected_hobi' : None})