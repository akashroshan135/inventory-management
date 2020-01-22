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

#contains the purchases made
class Purchase(models.Model):
    billno = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now=True)
    supplier = models.ForeignKey(Supplier, on_delete = models.CASCADE, related_name='purchasesupplier')
    stock = models.ForeignKey(Stock, on_delete = models.CASCADE, related_name='purchasestock')
    quantity = models.IntegerField(default=1)

    def __str__(self):
	    return self.billno