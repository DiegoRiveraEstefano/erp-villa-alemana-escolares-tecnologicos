from django.urls import path

from .views import customer_create_view
from .views import customer_delete_view
from .views import customer_detail_view
from .views import customer_list_view
from .views import customer_update_view

app_name = "customers"
urlpatterns = [
    path("customer/", view=customer_list_view, name="customer-list"),
    path("customer/create/", view=customer_create_view, name="customer-create"),
    path("customer/delete/<str:pk>", view=customer_delete_view, name="customer-delete"),
    path("customer/update/<str:pk>", view=customer_update_view, name="customer-update"),
    path(
        "customer/detail/<str:pk>/",
        view=customer_detail_view,
        name="customer-detail",
    ),
]
