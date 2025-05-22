from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Sale
from .models import SaleItem


class SaleCreateForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = (
            "customer",
            "store",
            "total_price",
            "payment_method",
            "status",
        )


class SaleUpdateForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = (
            "customer",
            "store",
            "total_price",
            "payment_method",
            "status",
        )


class SaleDeleteForm(forms.ModelForm):
    confirmation = forms.BooleanField(label=_("confirmation"), required=False)

    class Meta:
        model = Sale
        fields = ()


class SaleItemCreateForm(forms.ModelForm):
    class Meta:
        model = SaleItem
        fields = (
            "sale",
            "product",
            "quantity",
        )


class SaleItemUpdateForm(forms.ModelForm):
    class Meta:
        model = SaleItem
        fields = (
            "sale",
            "product",
            "quantity",
        )


class SaleItemDeleteForm(forms.ModelForm):
    confirmation = forms.BooleanField(label=_("confirmation"), required=False)

    class Meta:
        model = SaleItem
        fields = ()
