from django.core.validators import BaseValidator
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _

from erp_villa_alemana_escolares_tecnologicos.apps.employees.tasks import validate_rut


@deconstructible
class RutValidator(BaseValidator):
    """
    Validator for Chilean RUT (Rol Único Tributario).
    """

    message = _("Enter a valid RUT.")
    code = "invalid_rut"

    def compare(self, a, b):
        return validate_rut(a)
