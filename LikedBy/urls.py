from django.urls import path

from . import views

app_name = 'likedBy'

urlpatterns = [
    path('', views.get_list_liked_by, name=''),
]
