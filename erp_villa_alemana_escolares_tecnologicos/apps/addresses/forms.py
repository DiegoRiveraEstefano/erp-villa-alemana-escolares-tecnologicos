from django import forms
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

from erp_villa_alemana_escolares_tecnologicos.apps.addresses.validators import (
    POSTAL_CODE_REGEX,
)

from .models import Address
from .models import Comuna


class AddressCreateForm(forms.ModelForm):
    comuna = forms.ModelChoiceField(
        queryset=Comuna.objects.all(),
        label=_("Comuna"),
        required=False,
        help_text=_("Select the comuna."),
    )

    postal_code = forms.CharField(
        max_length=10,
        label=_("Postal Code"),
        required=False,
        help_text=_("Enter the postal code for the address."),
        validators=[
            RegexValidator(
                regex=POSTAL_CODE_REGEX,
                message=_("Postal code must be between 4 and 10 digits."),
            ),
        ],
        widget=forms.TextInput(
            attrs={
                "placeholder": _("Postal Code"),
                "pattern": POSTAL_CODE_REGEX,
            },
        ),
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
