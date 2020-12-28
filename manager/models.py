from django.db import models

class Goods(models.Model):
    name = models.CharField(max_length=200)
#    price = models.IntegerField()
    qty = models.IntegerField()


class Balance(models.Model):
    'saldo'
    sum = models.IntegerField()
    commentary = models.CharField(max_length=800, default=None)

class Overview(models.Model):
    'przegląd'
    action = models.CharField(max_length=1000)
    x = models.ForeignKey('Goods', on_delete=models.PROTECT)

    # def __str__(self):
    #     return self.name
