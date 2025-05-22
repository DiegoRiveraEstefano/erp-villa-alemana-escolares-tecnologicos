from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Product
from .models import ProductCategory


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ()


class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ()


class ProductDeleteForm(forms.ModelForm):
    confirmation = forms.BooleanField(label=_("confirmation"), required=False)

    class Meta:
        model = Product
        fields = ()


class ProductCategoryCreateForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ()


class ProductCategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ()


class ProductCategoryDeleteForm(forms.ModelForm):
    confirmation = forms.BooleanField(label=_("confirmation"), required=False)

    class Meta:
        model = ProductCategory
        fields = ()
