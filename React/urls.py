from django.urls import path
from React import views

app_name = 'react'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('like/<str:user>', views.like, name='like'),
    path('dislike/', views.dislike, name='dislike')
]