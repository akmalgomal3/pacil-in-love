from django.urls import path

from . import views

app_name = 'profile'

urlpatterns = [
    path('profile', views.profile, name='profile'),
    path('create_profile', views.createProfilePage, name='create_profile'),
    path('update_profile', views.updateProfilePage, name='update_profile'),
    path('update_auth', views.updatePasswordPage, name='update_auth'),
]