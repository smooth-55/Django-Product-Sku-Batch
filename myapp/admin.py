from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Sku)
admin.site.register(models.Product)
admin.site.register(models.Batch)