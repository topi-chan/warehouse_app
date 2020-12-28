from django.db import models

class Goods(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    qty = models.IntegerField()

    # def __str__(self):
    #     return self.name
