from django.db import models
from inventory.models import Stock

#contains suppliers
class Supplier(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=12, unique=True)
    email = models.EmailField(max_length=254)

    def __str__(self):
	    return self.name

#contains the purchase bills made
class PurchaseBill(models.Model):
    billno = models.AutoField(primary_key=True)
    time = models.DateTimeField(auto_now=True)
    supplier = models.ForeignKey(Supplier, on_delete = models.CASCADE, related_name='purchasesupplier')

    def __int__(self):
	    return self.billno

#contains the purchase stocks made
class PurchaseStock(models.Model):
    billno = models.ForeignKey(PurchaseBill, on_delete = models.CASCADE, related_name='purchasebillno')
    stock = models.ForeignKey(Stock, on_delete = models.CASCADE, related_name='purchasestocksupplier')
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=1)

    def __int__(self):
	    return self.billno