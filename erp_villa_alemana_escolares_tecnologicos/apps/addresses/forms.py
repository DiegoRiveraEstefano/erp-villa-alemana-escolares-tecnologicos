from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Address
from .models import Comuna


class AddressCreateForm(forms.ModelForm):
    comuna = forms.ModelChoiceField(
        queryset=Comuna.objects.all(),
        label=_("Comuna"),
        required=False,
        help_text=_("Select the comuna."),
    )

    class Meta:
        model = Address
        fields = (
            "street",
            "number",
            "postal_code",
            "apartment",
            "floor",
            "description",
            "comuna",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class AddressUpdateForm(forms.ModelForm):
    comuna = forms.ModelChoiceField(
        queryset=Comuna.objects.all(),
        label=_("Comuna"),
        required=False,
        help_text=_("Select the comuna."),
    )

    class Meta:
        model = Address
        fields = (
            "street",
            "number",
            "postal_code",
            "apartment",
            "floor",
            "description",
            "comuna",
        )


class AddressDeleteForm(forms.ModelForm):
    confirmation = forms.BooleanField(label=_("confirmation"), required=False)

    class Meta:
        model = Address
        fields = ()
