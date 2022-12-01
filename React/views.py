from django.db import connection
from django.shortcuts import redirect, render

# Create your views here.
def index(request):
    return redirect("home:index")
    
def like(request):
    data = request.POST
    cursor = connection.cursor()
    cursor.execute("set search_path to public")
    
    username = request.session['username']
    role = request.session['role']
    
    cursor.execute("set search_path to tkyry")
    
    return render(request)

def dislike(request):
    data = request.POST
    cursor = connection.cursor()
    cursor.execute("set search_path to public")
    
    username = request.session['username']
    role = request.session['role']
    
    cursor.execute("set search_path to tkyry")
    
    return render(request)