from django.db import models

#contains the category
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
#contains the details of the stock
class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField(default=0)

    def __str__(self):
	    return self.name

#contains the purchases made
class Purchases(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField(default=0)

    def __str__(self):
	    return self.name