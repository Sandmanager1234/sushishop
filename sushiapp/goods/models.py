from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)


class Good(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, blank=True, null=True)
    picture = models.ImageField(upload_to='goods_images', blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    discount = models.DecimalField(max_length=4, decimal_places=2, default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    is_available = models.BooleanField(default=True)

    def final_price(self):
        return self.price - self.price * self.discount / 100
