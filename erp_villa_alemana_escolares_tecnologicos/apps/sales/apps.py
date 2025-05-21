import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SalesConfig(AppConfig):
    """
    Configuration class for the Sales app.
    """

    name = "erp_villa_alemana_escolares_tecnologicos.apps.sales"
    verbose_name = _("Sales")

    def ready(self):
        """
        Import signals when the app is ready.
        """
        with contextlib.suppress(ImportError):
            import erp_villa_alemana_escolares_tecnologicos.sales.signals  # noqa: F401
