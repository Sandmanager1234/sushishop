from django.db import models

from goods.models import Category
from users.models import User


class Promo(models.Model):
    DISCOUNT_TYPES = (
        (1, 'Percents'),
        (2, 'Simple')
    )
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=2047)
    promocode = models.CharField(max_length=20)
    banner = models.ImageField(upload_to='promo_banners')
    discount_type = models.SmallIntegerField(choices=DISCOUNT_TYPES)
    category = models.ForeignKey(Category)
    discount = models.DecimalField(max_digits=7, decimal_places=2)
    start_promo = models.DateField(auto_now_add=True)
    end_promo = models.DateField(blank=True, null=True)


class PromoUserRelation(models.Model):
    user = models.ForeignKey(User)
    promo = models.ForeignKey(Promo)
    is_activated = models.BooleanField(default=False)


