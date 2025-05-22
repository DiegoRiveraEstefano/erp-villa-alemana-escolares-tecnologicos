from django import forms
from django.utils.translation import gettext_lazy as _

from erp_villa_alemana_escolares_tecnologicos.apps.employees.models import Employee
from erp_villa_alemana_escolares_tecnologicos.apps.warehouses.models import Warehouse

from .models import Store
from .models import StoreEmployee


class StoreCreateForm(forms.ModelForm):
    warehouse = forms.ModelChoiceField(
        queryset=Warehouse.objects.all(),
        required=True,
        label=_("Warehouse"),
        help_text=_("The warehouse associated with the store."),
    )

    class Meta:
        model = Store
        fields = (
            "name",
            "slug",
            "description",
            "type",
            "warehouse",
        )


class StoreUpdateForm(forms.ModelForm):
    warehouse = forms.ModelChoiceField(
        queryset=Warehouse.objects.all(),
        required=True,
        label=_("Warehouse"),
        help_text=_("The warehouse associated with the store."),
    )

    class Meta:
        model = Store
        fields = (
            "name",
            "slug",
            "description",
            "type",
            "warehouse",
        )


class StoreDeleteForm(forms.ModelForm):
    confirmation = forms.BooleanField(label=_("confirmation"), required=False)

    class Meta:
        model = Store
        fields = ()


class StoreEmployeeCreateForm(forms.ModelForm):
    store = forms.ModelChoiceField(
        queryset=Store.objects.all(),
        required=True,
        label=_("Store"),
        help_text=_("The store associated with the employee."),
    )
    employee = forms.ModelChoiceField(
        queryset=Employee.objects.all(),
        required=True,
        label=_("Employee"),
        help_text=_("The employee associated with the store."),
    )

    class Meta:
        model = StoreEmployee
        fields = (
            "store",
            "employee",
        )


class StoreEmployeeUpdateForm(forms.ModelForm):
    store = forms.ModelChoiceField(
        queryset=Store.objects.all(),
        required=True,
        label=_("Store"),
        help_text=_("The store associated with the employee."),
    )
    employee = forms.ModelChoiceField(
        queryset=Employee.objects.all(),
        required=True,
        label=_("Employee"),
        help_text=_("The employee associated with the store."),
    )

    class Meta:
        model = StoreEmployee
        fields = (
            "store",
            "employee",
        )


class StoreEmployeeDeleteForm(forms.ModelForm):
    confirmation = forms.BooleanField(label=_("confirmation"), required=False)

    class Meta:
        model = StoreEmployee
        fields = ()
