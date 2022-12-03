from django.urls import path

from . import views

app_name = 'auth'

urlpatterns = [
    path('', views.redirectLogin, name=''),
    path('login', views.loginPage, name='login'),
    path('register', views.registerPage, name='register'),
    path('logout', views.logout, name='logout')
]
