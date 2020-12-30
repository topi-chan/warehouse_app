from django.urls import path

from . import views
#app_name = 'manager'

urlpatterns = [
    path('', views.index, name='index'),
    path('saldo', views.saldo, name='saldo'),
    path('hub', views.hub, name='zakup'),
    path('review', views.przeglad, name='review')
]
