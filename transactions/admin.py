from django.contrib import admin
from .models import (
    Supplier, 
    PurchaseBill, 
    PurchaseItem, 
    SaleBill, 
    SaleItem
)

admin.site.register(Supplier)
admin.site.register(PurchaseBill)
admin.site.register(PurchaseItem)
admin.site.register(SaleBill)
admin.site.register(SaleItem)