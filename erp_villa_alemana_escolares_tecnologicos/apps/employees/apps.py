import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class EmployeesConfig(AppConfig):
    """
    Configuration class for the Employees app.
    """

    name = "erp_villa_alemana_escolares_tecnologicos.apps.employees"
    verbose_name = _("Employees")

    def ready(self):
        """
        Import signals when the app is ready.
        """
        with contextlib.suppress(ImportError):
            import erp_villa_alemana_escolares_tecnologicos.employees.signals  # noqa: F401
