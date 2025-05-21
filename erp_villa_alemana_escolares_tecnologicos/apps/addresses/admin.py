from django.contrib import admin

from erp_villa_alemana_escolares_tecnologicos.apps.addresses.models import Address
from erp_villa_alemana_escolares_tecnologicos.apps.addresses.models import Comuna
from erp_villa_alemana_escolares_tecnologicos.apps.addresses.models import Province
from erp_villa_alemana_escolares_tecnologicos.apps.addresses.models import Region

admin.site.register(Address)
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(Province)
