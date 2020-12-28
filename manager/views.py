from django.http import HttpResponse
from django.shortcuts import render, redirect
from manager.py_mg.mg import *
from manager.models import *

def index(request):
#    print(request.POST["Komentarz"])
    one_entry = Balance.objects.get(pk=1)
    value_of_entry = one_entry.sum
    return render(request, 'manager/index.html', {"saldo":value_of_entry})

def saldo(request):
    index_sum = request.POST['zmiana']
    index_commentary = request.POST['Komentarz']
    s = Balance(sum = int(index_sum), commentary = index_commentary)
    return redirect('index')

#w render przekazać parametr oprócz request można jeszcze kolejne argsy
#i to muszą być nazwane parametry

    #Goods.objects.all() to wywołanie wszystkich pozycji - poczytać w dokumentacji
    # all_entries = Goods.objects.all()
    # {"magazyn":all_entries}
    # dla listy przedmiotów? i potem jinja w html
