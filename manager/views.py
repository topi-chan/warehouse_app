from django.http import HttpResponse
from django.shortcuts import render, redirect
from manager.models import *

def index(request):
    if Balance.objects.count() > 0:
        correct_entry = Balance.objects.last()
        value_of_entry = correct_entry.sum
    else:
        value_of_entry = "Brak środków na koncie - 0"
    all_entries = Storage.objects.all()
    context = {"saldo":value_of_entry, "magazyn":all_entries}
    if 'error' in request.session:
        context['error'] = request.session['error']
        del request.session['error']
    return render(request, 'manager/index.html', context)

def saldo(request):
    index_sum = request.POST['zmiana']
    index_commentary = request.POST['Komentarz']
    if Balance.objects.count() > 0:
        balance_last = Balance.objects.last()
        balance_add = Balance(sum = balance_last.sum + int(index_sum),
            commentary = index_commentary, current = int(index_sum))
    else:
        balance_add = Balance(sum = int(index_sum),
            commentary = index_commentary, current = int(index_sum))
    balance_add.save()
    log = Overview(balance = balance_add)
    log.save()
    return redirect('index')

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
    if (price * pieces) <= balance_total.sum:
        if Storage.objects.filter(name = request.POST['nazwa']) is True:
            goods_object = Storage.objects.get(name = request.POST['nazwa'])
            qty1 = goods_object.qty + pieces
            Storage.objects.filter(name=request.POST['nazwa']).update(qty=qty1)
        else:
            goods_add = Storage(name = request.POST['nazwa'], qty = pieces)
            goods_add.save()
        log_add = StorageLog(name = request.POST['nazwa'], qty = pieces,
            price = price, action_type = "zakup")
        log_add.save()
        balance_total.sum = balance_total.sum - (price*pieces)
        balance_total.save()
        log = Overview(storage_log = log_add)
        log.save()
        return redirect('index')
    else:
        request.session['error'] = "Brak środków na koncie"
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
    if Storage.objects.filter(name = request.POST['nazwa']).exists():
        goods_object = Storage.objects.get(name = request.POST['nazwa'])
        qty1 = goods_object.qty - pieces
        if qty1 < 0:
            request.session['error'] = "Brak tylu produktów w magazynie"
            return redirect('index')
        Storage.objects.filter(name=request.POST['nazwa']).update(qty=qty1)
        log_add = StorageLog(name = request.POST['nazwa'], qty = pieces,
            price = price, action_type = "sprzedaż")
        if qty1 == 0:
            log_add.delete()
            return redirect('index')
        log_add.save()
        balance_total = Balance.objects.last()
        balance_total.sum = balance_total.sum + (price*pieces)
        balance_total.save()
        log = Overview(storage_log = log_add)
        log.save()
        return redirect('index')
    else:
        request.session['error'] = "Brak produktu w magazynie"
        return redirect('index')

def hub(request):
    if request.POST['wybor'] == 'sprzedaz':
        return sprzedaz(request)
    if request.POST['wybor'] == 'zakup':
        return zakup(request)

def przeglad(request):
    przeglad = Overview.objects.all()
    context = {"przeglad":przeglad}
    return render(request, 'manager/review.html', context)
