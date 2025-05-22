from django import template

register = template.Library()


@register.filter
def split(word, sep=","):
    assert isinstance(word, str), "The model must be a string"
    return word.split(sep)


@register.filter
def join(word, sep=","):
    assert isinstance(word, list), "The model must be a list"
    return sep.join(word)


@register.filter
def replace(word, args):
    assert isinstance(word, str), "The model must be a string"
    assert isinstance(args, list), "The args must be a list"
    assert len(args) == 2, "The args must be a list of two elements"
    return word.replace(args[0], args[1])
