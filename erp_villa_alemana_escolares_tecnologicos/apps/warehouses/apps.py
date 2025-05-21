import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class WarehouseConfig(AppConfig):
    name = "erp_villa_alemana_escolares_tecnologicos.apps.warehouses"
    verbose_name = _("Warehouses")

    def ready(self):
        with contextlib.suppress(ImportError):
            import erp_villa_alemana_escolares_tecnologicos.warehouses.signals  # noqa: F401
