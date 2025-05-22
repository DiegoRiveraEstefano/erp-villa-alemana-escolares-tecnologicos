from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Store
from .models import StoreEmployee


class StoreCreateForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ()


class StoreUpdateForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ()


class StoreDeleteForm(forms.ModelForm):
    confirmation = forms.BooleanField(label=_("confirmation"), required=False)

    class Meta:
        model = Store
        fields = ()


class StoreEmployeeCreateForm(forms.ModelForm):
    class Meta:
        model = StoreEmployee
        fields = ()


class StoreEmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model = StoreEmployee
        fields = ()


class StoreEmployeeDeleteForm(forms.ModelForm):
    confirmation = forms.BooleanField(label=_("confirmation"), required=False)

    class Meta:
        model = StoreEmployee
        fields = ()
