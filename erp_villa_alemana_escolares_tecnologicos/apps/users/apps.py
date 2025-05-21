import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "erp_villa_alemana_escolares_tecnologicos.apps.users"
    verbose_name = _("Users")

    def ready(self):
        with contextlib.suppress(ImportError):
            import erp_villa_alemana_escolares_tecnologicos.apps.users.signals  # noqa: F401
