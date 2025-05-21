import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class StoresConfig(AppConfig):
    """
    Configuration class for the Stores app.
    """

    name = "erp_villa_alemana_escolares_tecnologicos.apps.stores"
    verbose_name = _("Stores")

    def ready(self):
        """
        Import signals when the app is ready.
        """
        with contextlib.suppress(ImportError):
            import erp_villa_alemana_escolares_tecnologicos.stores.signals  # noqa: F401
