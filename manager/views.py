from django.http import HttpResponse
from django.shortcuts import render, redirect
# from manager.py_mg.mg import *
from manager.models import *

def index(request):
    correct_entry = Balance.objects.last()
    value_of_entry = correct_entry.sum
    all_entries = StorageLog.objects.all()
    context = {"saldo":value_of_entry, "magazyn":all_entries}
    if 'error' in request.session:
        context['error'] = request.session['error']
        del request.session['error']
    return render(request, 'manager/index.html', context)
#poczytać o sesjach
def saldo(request):
    index_sum = request.POST['zmiana']
    index_commentary = request.POST['Komentarz']
    balance_last = Balance.objects.last()
    balance_add = Balance(sum = balance_last.sum + int(index_sum),
        commentary = index_commentary, current = int(index_sum))
    balance_add.save()
    return redirect('index')
# w saldo dodac overview

def zakup(request):
    price = int(request.POST['cena'])
    pieces = int(request.POST['sztuki'])
    if price < 0:
        request.session['error'] = "Cena nie może być mniejsza od 0"
        return redirect('index')
    if pieces < 0:
        request.session['error'] = "Liczba sztuk nie może być mniejsza od 0"
        return redirect('index')
    balance_total = Balance.objects.last()
#dodac wpis do storagelog , zaktualizowac storage i wpis do overview i tak samo w sprzedazy
    if (price * pieces) <= balance_total.sum:
        goods_add = Goods(name = request.POST['nazwa'], qty = pieces)
        goods_add.save()
        balance_total.sum = balance_total.sum - (price*pieces)
        balance_total.save()
        return redirect('index')
    else:
        return redirect('index')

def sprzedaz(request):
    price = int(request.POST['cena'])
    pieces = int(request.POST['sztuki'])
    if price < 0:
        request.session['error'] = "Cena nie może być mniejsza od 0"
        return redirect('index')
    if pieces < 0:
        request.session['error'] = "Liczba sztuk nie może być mniejsza od 0"
        return redirect('index')
    if Goods.objects.filter(name = request.POST['nazwa']) is True:
        goods_object = Goods.objects.get(name = request.POST['nazwa'])
        qty1 = goods_object.name + pieces
        Goods.objects.filter(pk=request.POST['nazwa']).update(qty=qty1)
        balance_total = Balance.objects.get(pk=1)
        balance_total.sum = balance_total.sum + (price*pieces)
        balance_total.save()
        return redirect('index')
    else:
        return redirect('index')

def hub(request):
    if request.POST['wybor'] == 'sprzedaz':
        return sprzedaz(request)
    if request.POST['wybor'] == 'zakup':
        return zakup(request)
