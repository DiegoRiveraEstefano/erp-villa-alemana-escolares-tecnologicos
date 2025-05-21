import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CustomersConfig(AppConfig):
    """
    Configuration class for the Customers app.
    """

    name = "erp_villa_alemana_escolares_tecnologicos.apps.customers"
    verbose_name = _("Customers")

    def ready(self):
        """
        Import signals when the app is ready.
        """
        with contextlib.suppress(ImportError):
            import erp_villa_alemana_escolares_tecnologicos.customers.signals  # noqa: F401
