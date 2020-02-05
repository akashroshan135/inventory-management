from django.db import models
from inventory.models import Stock

#contains suppliers TODO: add new fields
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

    def __str__(self):
	    return "Bill no: " + str(self.billno)

    def get_items_list(self):
        return PurchaseItem.objects.filter(billno=self)

#contains the purchase stocks made
class PurchaseItem(models.Model):
    billno = models.ForeignKey(PurchaseBill, on_delete = models.CASCADE, related_name='purchasebillno')
    stock = models.ForeignKey(Stock, on_delete = models.CASCADE, related_name='purchaseitem')
    quantity = models.IntegerField(default=1)
    perprice = models.IntegerField(default=1)
    totalprice = models.IntegerField(default=1)

    def __str__(self):
	    return "Bill no: " + str(self.billno.billno) + ", Item = " + self.stock.name


#contains the sale bills made TODO: add new fields
class SaleBill(models.Model):
    billno = models.AutoField(primary_key=True)
    time = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=254, blank=True)

    def __str__(self):
	    return "Bill no: " + str(self.billno)

    def get_items_list(self):
        return SaleItem.objects.filter(billno=self)

#contains the sale stocks made
class SaleItem(models.Model):
    billno = models.ForeignKey(SaleBill, on_delete = models.CASCADE, related_name='salebillno')
    stock = models.ForeignKey(Stock, on_delete = models.CASCADE, related_name='saleitem')
    quantity = models.IntegerField(default=1)
    perprice = models.IntegerField(default=1)
    totalprice = models.IntegerField(default=1)

    def __str__(self):
	    return "Bill no: " + str(self.billno.billno) + ", Item = " + self.stock.name