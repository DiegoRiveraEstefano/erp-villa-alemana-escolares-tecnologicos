from django.urls import path

from .views import product_create_view
from .views import product_delete_view
from .views import product_detail_view
from .views import product_list_view
from .views import product_update_view

app_name = "products"
urlpatterns = [
    path("product/", view=product_list_view, name="product-list"),
    path("product/create/", view=product_create_view, name="product-create"),
    path("product/delete/<int:pk>", view=product_delete_view, name="product-delete"),
    path("product/update/<int:pk>", view=product_update_view, name="product-update"),
    path("product/detail/<int:pk>/", view=product_detail_view, name="product-detail"),
]
