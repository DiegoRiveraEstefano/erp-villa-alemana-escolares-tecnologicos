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
    department = forms.ModelChoiceField(
        queryset=EmployeeDepartment.objects.all(),
        required=True,
        label=_("Department"),
        help_text=_("The department associated with the employee."),
    )
    position = forms.ModelChoiceField(
        queryset=EmployeePosition.objects.all(),
        required=True,
        label=_("Position"),
        help_text=_("The position associated with the employee."),
    )

    class Meta:
        model = Employee
        fields = (
            "department",
            "position",
            "hire_date",
            "is_active",
            "salary",
            "first_name",
            "last_name",
            "email",
            "phone_number",
        )


class EmployeeUpdateForm(forms.ModelForm):
    department = forms.ModelChoiceField(
        queryset=EmployeeDepartment.objects.all(),
        required=True,
        label=_("Department"),
        help_text=_("The department associated with the employee."),
    )
    position = forms.ModelChoiceField(
        queryset=EmployeePosition.objects.all(),
        required=True,
        label=_("Position"),
        help_text=_("The position associated with the employee."),
    )

    class Meta:
        model = Employee
        fields = (
            "department",
            "position",
            "hire_date",
            "is_active",
            "salary",
            "first_name",
            "last_name",
            "email",
            "phone_number",
        )


class EmployeeDeleteForm(forms.ModelForm):
    confirmation = forms.BooleanField(label=_("confirmation"), required=False)

    class Meta:
        model = Employee
        fields = ()


class EmployeeDepartmentCreateForm(forms.ModelForm):
    class Meta:
        model = EmployeeDepartment
        fields = (
            "name",
            "slug",
            "description",
        )


class EmployeeDepartmentUpdateForm(forms.ModelForm):
    class Meta:
        model = EmployeeDepartment
        fields = (
            "name",
            "slug",
            "description",
        )


class EmployeeDepartmentDeleteForm(forms.ModelForm):
    confirmation = forms.BooleanField(label=_("confirmation"), required=False)

    class Meta:
        model = EmployeeDepartment
        fields = ()


class EmployeePositionCreateForm(forms.ModelForm):
    class Meta:
        model = EmployeePosition
        fields = (
            "name",
            "slug",
            "description",
        )


class EmployeePositionUpdateForm(forms.ModelForm):
    class Meta:
        model = EmployeePosition
        fields = (
            "name",
            "slug",
            "description",
        )


class EmployeePositionDeleteForm(forms.ModelForm):
    confirmation = forms.BooleanField(label=_("confirmation"), required=False)

    class Meta:
        model = EmployeePosition
        fields = ()
