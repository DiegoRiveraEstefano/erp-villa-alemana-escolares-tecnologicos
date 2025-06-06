from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Product
from .models import ProductCategory


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            "name",
            "slug",
            "description",
            "category",
            "price",
        )


class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            "name",
            "slug",
            "description",
            "category",
            "price",
        )


class ProductDeleteForm(forms.ModelForm):
    confirmation = forms.BooleanField(label=_("confirmation"), required=False)

    class Meta:
        model = Product
        fields = ()


class ProductCategoryCreateForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = (
            "name",
            "slug",
            "description",
        )


class ProductCategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = (
            "name",
            "slug",
            "description",
        )


class ProductCategoryDeleteForm(forms.ModelForm):
    confirmation = forms.BooleanField(label=_("confirmation"), required=False)

    class Meta:
        model = ProductCategory
        fields = ()
