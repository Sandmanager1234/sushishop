from django.db import models

from users.models import User
from goods.models import Good

# Create your models here.

class CartQuerySet(models.QuerySet):
    
    def total_price(self):
        return sum(cart.goods_price() for cart in self)
    
    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0
    

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    good = models.ForeignKey(Good, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)
    session_key = models.CharField(max_length=32, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True)