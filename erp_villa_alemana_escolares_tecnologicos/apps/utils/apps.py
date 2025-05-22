import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UtilsConfig(AppConfig):
    """
    Configuration class for the Utils app.
    """

    name = "erp_villa_alemana_escolares_tecnologicos.apps.utils"
    verbose_name = _("Utils")

    def ready(self):
        """
        Import signals when the app is ready.
        """
        with contextlib.suppress(ImportError):
            import erp_villa_alemana_escolares_tecnologicos.utils.signals  # noqa: F401
