from django import template
from django.db import models

register = template.Library()


@register.filter
def get_attribute(obj, attr):
    """Gets an attribute from an object and handles related managers"""
    try:
        value = getattr(obj, attr)
        if isinstance(value.__class__.objects, models.Manager):
            return ", ".join(str(item) for item in value.all())
    except Exception:
        return None
    return value


@register.filter
def get_model_fields(model):
    """Returns visible fields for the model (excluding auto fields and many-to-many)"""

    return [
        field
        for field in model._meta.get_fields()
        if not field.auto_created
        and not (field.many_to_many and not field.one_to_many)
        and not field.one_to_many
    ]
