from django.db import models

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=55)
    buying_price=models.IntegerField()
    seling_price=models.IntegerField()
    wholesale_price=models.IntegerField()
    quantity=models.IntegerField()
    reoder_level=models.IntegerField()
    
    def __str__(self):
        return self.name
