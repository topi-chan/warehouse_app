from django.urls import path

from . import views
#app_name = 'manager'

urlpatterns = [
    path('', views.index, name='index'),
    path('saldo', views.saldo, name='saldo'),
    path('zakup', views.zakup, name='zakup'),
    path('sprzedaz', views.zakup, name='sprzedaz')
]
