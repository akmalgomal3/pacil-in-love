from django.urls import path

from . import views

app_name = 'report'

urlpatterns = [
    path('reported-list/', views.list_reported, name='List Reported'),
    path('user/<str:pengguna>', views.report, name='report')
]