from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from erp_villa_alemana_escolares_tecnologicos.apps.utils.mixins import ModelContextMixin

from .forms import ProductCategoryCreateForm
from .forms import ProductCategoryDeleteForm
from .forms import ProductCategoryUpdateForm
from .forms import ProductCreateForm
from .forms import ProductDeleteForm
from .forms import ProductUpdateForm
from .models import Product
from .models import ProductCategory


class ProductDetailView(ModelContextMixin, PermissionRequiredMixin, DetailView):
    model = Product
    template_name = "products/product_detail.html"
    slug_field = "slug"
    slug_url_kwarg = "product_slug"
    context_object_name = "product"
    permission_required = "products.can_view_product"
    permission_denied_message = _("permission denied")


product_detail_view = ProductDetailView.as_view()


class ProductListView(ModelContextMixin, PermissionRequiredMixin, ListView):
    model = Product
    template_name = "products/product_list.html"
    context_object_name = "products"
    permission_required = "products.can_view_product"
    permission_denied_message = _("permission denied")


product_list_view = ProductListView.as_view()


class ProductCreateView(PermissionRequiredMixin, CreateView):
    model = Product
    template_name = "products/product_create.html"
    form_class = ProductCreateForm
    context_object_name = "product"
    permission_required = "products.can_add_product"
    permission_denied_message = _("permission denied")

    def get_success_url(self):
        """
        Get URL for product's detail view after creation.

        Returns:
            str: URL for product detail.
        """
        assert self.object is not None, "Object must be set before calling this method."
        return self.object.get_absolute_url()


product_create_view = ProductCreateView.as_view()


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    model = Product
    template_name = "products/product_update.html"
    form_class = ProductUpdateForm
    success_url = reverse_lazy("products:product-list")
    slug_field = "slug"
    slug_url_kwarg = "product_slug"
    context_object_name = "product"
    permission_required = "products.can_change_product"
    permission_denied_message = _("permission denied")


product_update_view = ProductUpdateView.as_view()


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    model = Product
    form_class = ProductDeleteForm
    template_name = "products/product_delete.html"
    success_url = reverse_lazy("products:product-list")
    slug_field = "slug"
    slug_url_kwarg = "product_slug"
    context_object_name = "product"
    permission_required = "products.can_delete_product"
    permission_denied_message = _("permission denied")


product_delete_view = ProductDeleteView.as_view()


class ProductCategoryDetailView(ModelContextMixin, PermissionRequiredMixin, DetailView):
    model = ProductCategory
    template_name = "products/category_detail.html"
    slug_field = "slug"
    slug_url_kwarg = "category_slug"
    context_object_name = "product_category"
    permission_required = "products.can_view_product_category"
    permission_denied_message = _("permission denied")


product_category_detail_view = ProductCategoryDetailView.as_view()


class ProductCategoryListView(ModelContextMixin, PermissionRequiredMixin, ListView):
    model = ProductCategory
    template_name = "products/category_list.html"
    context_object_name = "product_categories"
    permission_required = "products.can_view_product_category"
    permission_denied_message = _("permission denied")


product_category_list_view = ProductCategoryListView.as_view()


class ProductCategoryCreateView(PermissionRequiredMixin, CreateView):
    model = ProductCategory
    template_name = "products/category_create.html"
    form_class = ProductCategoryCreateForm
    success_url = reverse_lazy("products:category-list")
    context_object_name = "product_category"
    permission_required = "products.can_add_product_category"
    permission_denied_message = _("permission denied")


product_category_create_view = ProductCategoryCreateView.as_view()


class ProductCategoryUpdateView(PermissionRequiredMixin, UpdateView):
    model = ProductCategory
    template_name = "products/category_update.html"
    form_class = ProductCategoryUpdateForm
    success_url = reverse_lazy("products:category-list")
    context_object_name = "product_category"
    slug_field = "slug"
    slug_url_kwarg = "category_slug"
    permission_required = "products.can_change_product_category"
    permission_denied_message = _("permission denied")


product_category_update_view = ProductCategoryUpdateView.as_view()


class ProductCategoryDeleteView(PermissionRequiredMixin, DeleteView):
    model = ProductCategory
    form_class = ProductCategoryDeleteForm
    template_name = "products/category_delete.html"
    success_url = reverse_lazy("products:category-list")
    context_object_name = "product_category"
    slug_field = "slug"
    slug_url_kwarg = "category_slug"
    permission_required = "products.can_delete_product_category"
    permission_denied_message = _("permission denied")


product_category_delete_view = ProductCategoryDeleteView.as_view()
