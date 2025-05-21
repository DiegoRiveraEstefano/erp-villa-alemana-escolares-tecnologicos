from django.contrib import admin

from erp_villa_alemana_escolares_tecnologicos.apps.products.models import Product
from erp_villa_alemana_escolares_tecnologicos.apps.products.models import (
    ProductCategory,
)

admin.site.register(Product)
admin.site.register(ProductCategory)
