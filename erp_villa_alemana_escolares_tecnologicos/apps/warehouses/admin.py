from django.contrib import admin

from erp_villa_alemana_escolares_tecnologicos.apps.warehouses.models import Warehouse
from erp_villa_alemana_escolares_tecnologicos.apps.warehouses.models import (
    WarehouseEmployee,
)
from erp_villa_alemana_escolares_tecnologicos.apps.warehouses.models import (
    WarehouseInventory,
)

admin.site.register(Warehouse)
admin.site.register(WarehouseEmployee)
admin.site.register(WarehouseInventory)
