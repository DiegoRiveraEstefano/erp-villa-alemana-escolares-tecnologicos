from django.contrib import admin
from django.contrib.auth.models import Permission

from .models import User
from .models import UserGroup

admin.site.register(User)
admin.site.register(UserGroup)


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    """
    Admin view for the Permission model.
    """

    list_display = ("name", "codename")
    search_fields = ("name", "codename")
    list_filter = ("content_type",)
    ordering = ("name",)
