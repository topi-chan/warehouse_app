from django.contrib import admin


from .models import StorageLog, Balance, Overview, Storage

admin.site.register(StorageLog)
admin.site.register(Balance)
admin.site.register(Overview)
admin.site.register(Storage)
