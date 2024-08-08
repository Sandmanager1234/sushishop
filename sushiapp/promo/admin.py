from django.contrib import admin

from .models import Promo, PromoUserRelation


admin.site.register(Promo)
admin.site.register(PromoUserRelation)
