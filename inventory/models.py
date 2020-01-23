from django.db import models
    
#contains the details of the stock
class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    type = (
        ('t0', 'test0'),
        ('t1', 'test1'),
        ('t2', 'test2'),
        ('t3', 'test3'),
    )
    stock_type = models.CharField(max_length=2, choices=type)
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=255)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=1)

    def __str__(self):
	    return self.name