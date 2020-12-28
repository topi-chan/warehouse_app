from django.contrib import admin


from .models import Goods, Balance, Overview

admin.site.register(Goods)
admin.site.register(Balance)
admin.site.register(Overview)
