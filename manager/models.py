from django.db import models

class StorageLog(models.Model):
    name = models.CharField(max_length=800, default=None)
    price = models.IntegerField()
    qty = models.IntegerField()
    action_type = models.CharField(max_length=800, default=None)

    def __str__(self):
        return self.name


class Balance(models.Model):
    'saldo'
    sum = models.IntegerField()
    commentary = models.CharField(max_length=800, default=None)
    current = models.IntegerField(default=0)


class Overview(models.Model):
    'przegląd'
    storage_log = models.ForeignKey('StorageLog', on_delete=models.PROTECT, null=True)
    balance = models.ForeignKey('Balance', on_delete=models.PROTECT, null=True)


class Storage(models.Model):
    name = models.CharField(max_length=200)
    qty = models.IntegerField()

    def __str__(self):
        return self.name
