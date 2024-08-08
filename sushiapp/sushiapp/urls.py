"""
URL configuration for sushiapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('api/v1/goods/', include('goods.urls', namespace='goods')),
    path('api/v1/promo/', include('promo.urls', namespace='promo')),
]


# Struct
#
# www.site.com
# www.site.com/<category-name>
# www.site.com/<category-name>/<good-name>
# www.site.com/cart
# www.site.com/profile
# www.site.com/promo
# www.site.com/promo/<promo-name>
# www.site.com/accounts/login
# www.site.com/accounts/logout
# www.site.com/accounts/signup