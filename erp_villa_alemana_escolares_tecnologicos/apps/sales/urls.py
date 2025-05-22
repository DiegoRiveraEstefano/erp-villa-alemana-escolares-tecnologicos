from django.urls import path

from .views import sale_create_view
from .views import sale_delete_view
from .views import sale_detail_view
from .views import sale_list_view
from .views import sale_update_view

app_name = "sales"
urlpatterns = [
    path("sale/", view=sale_list_view, name="sale-list"),
    path("sale/create/", view=sale_create_view, name="sale-create"),
    path("sale/delete/<int:pk>", view=sale_delete_view, name="sale-delete"),
    path("sale/update/<int:pk>", view=sale_update_view, name="sale-update"),
    path(
        "sale/detail/<int:pk>/",
        view=sale_detail_view,
        name="sale-detail",
    ),
]
