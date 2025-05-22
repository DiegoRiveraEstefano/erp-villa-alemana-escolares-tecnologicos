from django import forms
from django.utils.translation import gettext_lazy as _

from erp_villa_alemana_escolares_tecnologicos.apps.employees.models import Employee
from erp_villa_alemana_escolares_tecnologicos.apps.employees.models import (
    EmployeeDepartment,
)
from erp_villa_alemana_escolares_tecnologicos.apps.employees.models import (
    EmployeePosition,
)


class EmployeeCreateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ()


class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ()


class EmployeeDeleteForm(forms.ModelForm):
    confirmation = forms.BooleanField(label=_("confirmation"), required=False)

    class Meta:
        model = Employee
        fields = ()


class EmployeeDepartmentCreateForm(forms.ModelForm):
    class Meta:
        model = EmployeeDepartment
        fields = ()


class EmployeeDepartmentUpdateForm(forms.ModelForm):
    class Meta:
        model = EmployeeDepartment
        fields = ()


class EmployeeDepartmentDeleteForm(forms.ModelForm):
    confirmation = forms.BooleanField(label=_("confirmation"), required=False)

    class Meta:
        model = EmployeeDepartment
        fields = ()


class EmployeePositionCreateForm(forms.ModelForm):
    class Meta:
        model = EmployeePosition
        fields = ()


class EmployeePositionUpdateForm(forms.ModelForm):
    class Meta:
        model = EmployeePosition
        fields = ()


class EmployeePositionDeleteForm(forms.ModelForm):
    confirmation = forms.BooleanField(label=_("confirmation"), required=False)

    class Meta:
        model = EmployeePosition
        fields = ()
