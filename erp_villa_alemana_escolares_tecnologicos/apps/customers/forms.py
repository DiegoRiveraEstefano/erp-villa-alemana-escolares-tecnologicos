from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Customer


class CustomerCreateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = (
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "rut",
            "customer_type",
            "customer_class",
        )


class CustomerUpdateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = (
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "rut",
            "customer_type",
            "customer_class",
        )


class CustomerDeleteForm(forms.ModelForm):
    confirmation = forms.BooleanField(label=_("confirmation"), required=False)

    class Meta:
        model = Customer
        fields = ()
