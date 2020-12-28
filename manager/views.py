from django.http import HttpResponse
from django.shortcuts import render, redirect
# from manager.py_mg.mg import *
from manager.models import *

def index(request):
    first_entry = Balance.objects.get(pk=1)
    value_of_entry = first_entry.sum
    all_entries = Goods.objects.all()
    context = {"saldo":value_of_entry, "magazyn":all_entries}
    return render(request, 'manager/index.html', context)

def saldo(request):
    index_sum = request.POST['zmiana']
    index_commentary = request.POST['Komentarz']
    balance_add = Balance(sum = int(index_sum), commentary = index_commentary)
    balance_add.save()
    balance_total = Balance.objects.get(pk=1)
    balance_total.sum = balance_total.sum + int(index_sum)
    balance_total.save()
    return redirect('index')

def zakup(request):
    price = int(request.POST['cena'])
    pieces = int(request.POST['sztuki'])
    if price < 0:
        return redirect('index')
    if pieces < 0:
        return redirect('index')
    balance_total = Balance.objects.get(pk=1)
    if (price * pieces) <= balance_total.sum:
        goods_add = Goods(name = request.POST['nazwa'], qty = pieces)
        goods_add.save()
        balance_total.sum = balance_total.sum - (price*pieces)
        balance_total.save()
        return redirect('index')
    else:
        return redirect('index')

# def sprzedaz(request):
#     price = int(request.POST['cena'])
#     pieces = int(request.POST['sztuki'])
#     if price < 0:
#         return redirect('index')
#     if pieces < 0:
#         return redirect('index')
#     if Goods.objects.filter(name = request.POST['nazwa']) is True:
#         goods_object = Goods.objects.get(name = request.POST['nazwa'])
#         qty1 = goods_object.name + pieces
#         Goods.objects.filter(pk=request.POST['nazwa']).update(qty=qty1)
#         balance_total = Balance.objects.get(pk=1)
#         balance_total.sum = balance_total.sum + (price*pieces)
#         balance_total.save()
#         return redirect('index')
#     else:
#         return redirect('index')
# '''https://stackoverflow.com/questions/28148883/
# django-get-list-of-objects-by-filtering-a-list-of-objects
# https://stackoverflow.com/questions/2712682/
# how-to-select-a-record-and-update-it-with-a-single-queryset-in-django'''




#w render przekazać parametr oprócz request można jeszcze kolejne argsy
#i to muszą być nazwane parametry
