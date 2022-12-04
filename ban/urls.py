from django.urls import path

from . import views

app_name = 'ban'

urlpatterns = [
    path('', views.banPage, name='ban'),
    path('delete_user/<str:username>', views.req_delete, name='delete_user'),
    path('timeout_user/<str:username>', views.req_timeout, name='timeout_user')
]