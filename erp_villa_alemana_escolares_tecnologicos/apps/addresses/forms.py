from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Address


class AddressCreateForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ()


class AddressUpdateForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ("pk",)


class AddressDeleteForm(forms.ModelForm):
    confirmation = forms.BooleanField(label=_("confirmation"), required=False)

    class Meta:
        model = Address
        fields = ("pk",)
