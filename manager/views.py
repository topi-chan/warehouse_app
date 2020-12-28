from django.http import HttpResponse
from django.shortcuts import render, redirect
from manager.py_mg.mg import *

def index(request):
#    print(request.POST["Komentarz"])
    return render(request, 'manager/index.html', {"saldo":0})
    #Goods.objects.all() to wywołanie wszystkich pozycji - poczytać w dokumentacji

def saldo(request):
    return redirect(request, 'index')

#w render przekazać parametr oprócz request można jeszcze kolejne argsy
#i to muszą być nazwane parametry
