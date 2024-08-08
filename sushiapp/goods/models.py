from django.db import models

from modules.services.utils import unique_slugify

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, blank=True, null=True, unique=True)

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = unique_slugify(self, self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Good(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True, null=True, unique=True)
    picture = models.ImageField(upload_to='goods_images', blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    discount = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    is_available = models.BooleanField(default=True)

    def final_price(self):
        return self.price - self.price * self.discount / 100
    
    # def is_discount(self):
    #     if self.discount:
    #         return True
    #     return False

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = unique_slugify(self, self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} {"Доступно" if self.is_available else "Нет в наличии"}'

