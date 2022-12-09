from django.http.response import JsonResponse, HttpResponse
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.db import connection
from Auth.forms import loginForm, registerForm
from Profile import *

# Create your views here.
def redirectHome(request):return render('Profile:profile')