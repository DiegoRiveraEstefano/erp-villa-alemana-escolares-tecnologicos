from django.contrib import admin

from erp_villa_alemana_escolares_tecnologicos.apps.sales.models import Sale
from erp_villa_alemana_escolares_tecnologicos.apps.sales.models import SaleItem

admin.site.register(Sale)
admin.site.register(SaleItem)
