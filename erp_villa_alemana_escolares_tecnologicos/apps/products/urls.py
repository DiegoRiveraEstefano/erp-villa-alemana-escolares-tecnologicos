from django.urls import path

from .views import product_category_create_view
from .views import product_category_delete_view
from .views import product_category_detail_view
from .views import product_category_list_view
from .views import product_category_update_view
from .views import product_create_view
from .views import product_delete_view
from .views import product_detail_view
from .views import product_list_view
from .views import product_update_view

app_name = "products"
urlpatterns = [
    path("product/", view=product_list_view, name="product-list"),
    path("product/create/", view=product_create_view, name="product-create"),
    path(
        "product/delete/<str:product_slug>",
        view=product_delete_view,
        name="product-delete",
    ),
    path(
        "product/update/<str:product_slug>",
        view=product_update_view,
        name="product-update",
    ),
    path(
        "product/detail/<str:product_slug>/",
        view=product_detail_view,
        name="product-detail",
    ),
    path(
        "category/",
        view=product_category_list_view,
        name="category-list",
    ),
    path(
        "category/create/",
        view=product_category_create_view,
        name="category-create",
    ),
    path(
        "category/delete/<str:category_slug>",
        view=product_category_delete_view,
        name="category-delete",
    ),
    path(
        "category/update/<str:category_slug>",
        view=product_category_update_view,
        name="category-update",
    ),
    path(
        "category/detail/<str:category_slug>/",
        view=product_category_detail_view,
        name="category-detail",
    ),
]
