import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ProductsConfig(AppConfig):
    """
    Configuration class for the Products app.
    """

    name = "erp_villa_alemana_escolares_tecnologicos.apps.products"
    verbose_name = _("Products")

    def ready(self):
        """
        Import signals when the app is ready.
        """
        with contextlib.suppress(ImportError):
            import erp_villa_alemana_escolares_tecnologicos.products.signals  # noqa: F401
