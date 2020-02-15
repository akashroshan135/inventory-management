from django.db import models
    
#contains the details of the stock FIXME: fix fields
class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=255)
    quantity = models.IntegerField(default=1)

    def __str__(self):
	    return self.name