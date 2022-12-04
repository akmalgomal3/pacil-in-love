from django.urls import path
from react import views

app_name = 'react'

urlpatterns = [
    path('', views.index, name = 'index'),
]