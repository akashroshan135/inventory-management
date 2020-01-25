from django.contrib import admin
from .models import Supplier, PurchaseBill, PurchaseItem

admin.site.register(Supplier)
admin.site.register(PurchaseBill)
admin.site.register(PurchaseItem)