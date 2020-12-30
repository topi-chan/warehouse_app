from django.db import models

class StorageLog(models.Model):
    item = models.ForeignKey('Storage', on_delete=models.PROTECT, null=True)
    price = models.IntegerField()
#    qty = models.IntegerField()
    action_type = models.CharField(max_length=800, default=None)

class Balance(models.Model):
    'saldo'
    sum = models.IntegerField()
    commentary = models.CharField(max_length=800, default=None)
    current = models.IntegerField(default=0)
#przy kazdym zakupie lub sprzedazy tworzenie nowego obiektu klasy balance
#w ktorym by byla zmiana salda jesli chce ;)
#wylistowac i zrobic ograniczenie dop np 30 wpisow

class Overview(models.Model):
    'przegląd'
#    action = models.CharField(max_length=1000)
    storage_log = models.ForeignKey('StorageLog', on_delete=models.PROTECT, null=True)
    balance = models.ForeignKey('Balance', on_delete=models.PROTECT, null=True)

class Storage(models.Model):
    name = models.CharField(max_length=200)
    qty = models.IntegerField()
    # def __str__(self):
    #     return self.name
