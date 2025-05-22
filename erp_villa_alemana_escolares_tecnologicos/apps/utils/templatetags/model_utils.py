from django import template

register = template.Library()


@register.filter
def get_attribute(obj, attr):
    """Gets an attribute from an object and handles related managers"""
    assert isinstance(attr, str), "attr must be a string "
    try:
        value = obj.__dict__[attr]
    except Exception as _:
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
