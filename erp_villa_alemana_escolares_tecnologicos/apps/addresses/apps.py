import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AddressesConfig(AppConfig):
    """
    Configuration class for the Addresses app.
    """

    name = "erp_villa_alemana_escolares_tecnologicos.apps.addresses"
    verbose_name = _("Addresses")

    def ready(self):
        """
        Import signals when the app is ready.
        """
        with contextlib.suppress(ImportError):
            import erp_villa_alemana_escolares_tecnologicos.addresses.signals  # noqa: F401
