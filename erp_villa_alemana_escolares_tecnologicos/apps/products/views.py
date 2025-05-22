from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from .forms import ProductCategoryCreateForm
from .forms import ProductCategoryUpdateForm
from .forms import ProductCreateForm
from .forms import ProductUpdateForm
from .models import Product
from .models import ProductCategory


class ProductDetailView(DetailView):
    model = Product
    template_name = "products/views/product_detail.html"
    slug_field = "pk"
    slug_url_kwarg = "pk"


product_detail_view = ProductDetailView.as_view()


class ProductListView(ListView):
    model = Product
    template_name = "products/views/product_list.html"

    def get_queryset(self):
        return super().get_queryset()


product_list_view = ProductListView.as_view()


class ProductCreateView(CreateView):
    model = Product
    template_name = "products/views/product_create.html"
    form_class = ProductCreateForm


product_create_view = ProductCreateView.as_view()


class ProductUpdateView(UpdateView):
    model = Product
    template_name = "products/views/product_update.html"
    form_class = ProductUpdateForm


product_update_view = ProductUpdateView.as_view()


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "products/views/product_delete.html"


product_delete_view = ProductDeleteView.as_view()


class ProductCategoryDetailView(DetailView):
    model = ProductCategory
    template_name = "products/views/product_category_detail.html"
    slug_field = "pk"
    slug_url_kwarg = "pk"
    context_object_name = "product_category"


product_category_detail_view = ProductCategoryDetailView.as_view()


class ProductCategoryListView(ListView):
    model = ProductCategory
    template_name = "products/views/product_category_list.html"
    context_object_name = "product_category"

    def get_queryset(self):
        return super().get_queryset()


product_category_list_view = ProductCategoryListView.as_view()


class ProductCategoryCreateView(CreateView):
    model = ProductCategory
    template_name = "products/views/product_category_create.html"
    form_class = ProductCategoryCreateForm
    success_url = reverse_lazy("products:category-list")
    context_object_name = "product_category"


product_category_create_view = ProductCategoryCreateView.as_view()


class ProductCategoryUpdateView(UpdateView):
    model = ProductCategory
    template_name = "products/views/product_category_update.html"
    form_class = ProductCategoryUpdateForm
    success_url = reverse_lazy("products:category-list")
    context_object_name = "product_category"


product_category_update_view = ProductCategoryUpdateView.as_view()


class ProductCategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = "products/views/product_category_delete.html"
    success_url = reverse_lazy("products:category-list")
    context_object_name = "product_category"


product_category_delete_view = ProductCategoryDeleteView.as_view()
