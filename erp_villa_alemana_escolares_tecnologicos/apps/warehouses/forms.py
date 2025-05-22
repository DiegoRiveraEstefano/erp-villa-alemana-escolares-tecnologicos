from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Warehouse
from .models import WarehouseEmployee
from .models import WarehouseInventory


class WarehouseCreateForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = ()


class WarehouseUpdateForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = ()


class WarehouseDeleteForm(forms.ModelForm):
    confirmation = forms.BooleanField(label=_("confirmation"), required=False)

    class Meta:
        model = Warehouse
        fields = ()


class WarehouseEmployeeCreateForm(forms.ModelForm):
    class Meta:
        model = WarehouseEmployee
        fields = ()


class WarehouseEmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model = WarehouseEmployee
        fields = ()


class WarehouseEmployeeDeleteForm(forms.ModelForm):
    confirmation = forms.BooleanField(label=_("confirmation"), required=False)

    class Meta:
        model = WarehouseEmployee
        fields = ()


class WarehouseInventoryCreateForm(forms.ModelForm):
    class Meta:
        model = WarehouseInventory
        fields = ()


class WarehouseInventoryUpdateForm(forms.ModelForm):
    class Meta:
        model = WarehouseInventory
        fields = ()


class WarehouseInventoryDeleteForm(forms.ModelForm):
    confirmation = forms.BooleanField(label=_("confirmation"), required=False)

    class Meta:
        model = WarehouseInventory
        fields = ()
