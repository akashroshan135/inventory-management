from django.contrib import admin
from .models import Supplier, PurchaseBill, PurchaseStock

admin.site.register(Supplier)
admin.site.register(PurchaseBill)
admin.site.register(PurchaseStock)