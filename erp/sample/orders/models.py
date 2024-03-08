# models.py
from django.db import models

class OrderDetail(models.Model):
    item_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    ext_price = models.DecimalField(max_digits=12, decimal_places=2, default=0 )


