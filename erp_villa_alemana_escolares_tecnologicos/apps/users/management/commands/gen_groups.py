import json

from django.contrib.auth.models import Permission
from django.core.management.base import BaseCommand

from erp_villa_alemana_escolares_tecnologicos.apps.users.models import UserGroup


class Command(BaseCommand):
    def handle(self, *args, **options):
        groups = json.load(
            open(
                "erp_villa_alemana_escolares_tecnologicos/apps/users/management/commands/groups.json",
                encoding="utf-8",
            ),
        )
        for group in groups:
            permissions = Permission.objects.filter(
                codename__in=group["permissions"],
            )
            self.stdout.write(
                self.style.NOTICE(
                    f"Creando grupo '{group['name']}' con permisos: {', '.join(permissions.values_list('codename', flat=True))}",
                ),
            )
            group, created = UserGroup.objects.get_or_create(
                name=group["name"],
                slug=group["slug"],
                defaults={
                    "description": group["description"],
                },
            )

            group.permissions.set(permissions)
            group.save()
            self.stdout.write(self.style.SUCCESS(f"Grupo '{group.name}' creado."))
        self.stdout.write(self.style.SUCCESS("Todos los grupos han sido creados."))
