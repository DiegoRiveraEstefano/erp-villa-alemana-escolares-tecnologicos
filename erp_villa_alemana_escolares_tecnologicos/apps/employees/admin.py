from django.contrib import admin

from erp_villa_alemana_escolares_tecnologicos.apps.employees.models import Employee
from erp_villa_alemana_escolares_tecnologicos.apps.employees.models import (
    EmployeeDepartment,
)
from erp_villa_alemana_escolares_tecnologicos.apps.employees.models import (
    EmployeePosition,
)

admin.site.register(Employee)
admin.site.register(EmployeeDepartment)
admin.site.register(EmployeePosition)
