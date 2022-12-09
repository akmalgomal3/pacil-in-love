from django.urls import path
from React import views

app_name = 'react'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('filter/', views.filter, name = 'filter'),
    path('like/<str:user>/<str:id_hobi>', views.like, name='like'),
    path('dislike/<str:id_hobi>', views.dislike, name='dislike'),
    path('<str:hobbyID>', views.filterHobby, name='filterHobby')
]