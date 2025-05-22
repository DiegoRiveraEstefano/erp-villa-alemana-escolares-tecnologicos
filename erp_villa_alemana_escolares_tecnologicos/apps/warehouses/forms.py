from django import forms
from django.utils.translation import gettext_lazy as _

from erp_villa_alemana_escolares_tecnologicos.apps.employees.models import Employee
from erp_villa_alemana_escolares_tecnologicos.apps.products.models import Product

from .models import Warehouse
from .models import WarehouseEmployee
from .models import WarehouseInventory


class WarehouseCreateForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = (
            "name",
            "slug",
            "description",
            "type",
        )


class WarehouseUpdateForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = (
            "name",
            "slug",
            "description",
            "type",
        )


class WarehouseDeleteForm(forms.ModelForm):
    confirmation = forms.BooleanField(label=_("confirmation"), required=False)

    class Meta:
        model = Warehouse
        fields = ()


class WarehouseEmployeeCreateForm(forms.ModelForm):
    warehouse = forms.ModelChoiceField(
        queryset=Warehouse.objects.all(),
        required=True,
        label=_("Warehouse"),
        help_text=_("The warehouse associated with the employee."),
    )

    employee = forms.ModelChoiceField(
        queryset=Employee.objects.all(),
        required=True,
        label=_("Employee"),
        help_text=_("The employee associated with the warehouse."),
    )

    class Meta:
        model = WarehouseEmployee
        fields = (
            "warehouse",
            "employee",
        )


class WarehouseEmployeeUpdateForm(forms.ModelForm):
    warehouse = forms.ModelChoiceField(
        queryset=Warehouse.objects.all(),
        required=True,
        label=_("Warehouse"),
        help_text=_("The warehouse associated with the employee."),
    )

    employee = forms.ModelChoiceField(
        queryset=Employee.objects.all(),
        required=True,
        label=_("Employee"),
        help_text=_("The employee associated with the warehouse."),
    )

    class Meta:
        model = WarehouseEmployee
        fields = (
            "warehouse",
            "employee",
        )


class WarehouseEmployeeDeleteForm(forms.ModelForm):
    confirmation = forms.BooleanField(label=_("confirmation"), required=False)

    class Meta:
        model = WarehouseEmployee
        fields = ()


class WarehouseInventoryCreateForm(forms.ModelForm):
    product = forms.ModelChoiceField(
        queryset=Product.objects.all(),
        required=True,
        label=_("Product"),
        help_text=_("The product associated with the warehouse inventory."),
    )
    warehouse = forms.ModelChoiceField(
        queryset=Warehouse.objects.all(),
        required=True,
        label=_("Warehouse"),
        help_text=_("The warehouse associated with the inventory."),
    )

    class Meta:
        model = WarehouseInventory
        fields = (
            "product",
            "quantity",
            "warehouse",
        )


class WarehouseInventoryUpdateForm(forms.ModelForm):
    product = forms.ModelChoiceField(
        queryset=Product.objects.all(),
        required=True,
        label=_("Product"),
        help_text=_("The product associated with the warehouse inventory."),
    )
    warehouse = forms.ModelChoiceField(
        queryset=Warehouse.objects.all(),
        required=True,
        label=_("Warehouse"),
        help_text=_("The warehouse associated with the inventory."),
    )

    class Meta:
        model = WarehouseInventory
        fields = (
            "product",
            "quantity",
            "warehouse",
        )


class WarehouseInventoryDeleteForm(forms.ModelForm):
    confirmation = forms.BooleanField(label=_("confirmation"), required=False)

    class Meta:
        model = WarehouseInventory
        fields = ()
