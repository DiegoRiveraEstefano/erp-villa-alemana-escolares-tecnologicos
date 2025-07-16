from django.urls import path

from .views import warehouse_create_view
from .views import warehouse_delete_view
from .views import warehouse_detail_view
from .views import warehouse_employee_create_view
from .views import warehouse_employee_delete_view
from .views import warehouse_employee_detail_view
from .views import warehouse_employee_list_view
from .views import warehouse_employee_update_view
from .views import warehouse_inventory_create_view
from .views import warehouse_inventory_delete_view
from .views import warehouse_inventory_detail_view
from .views import warehouse_inventory_list_view
from .views import warehouse_inventory_update_view
from .views import warehouse_list_view
from .views import warehouse_update_view

app_name = "warehouses"
urlpatterns = [
    path("warehouse/", view=warehouse_list_view, name="warehouse-list"),
    path("warehouse/create/", view=warehouse_create_view, name="warehouse-create"),
    path(
        "warehouse/delete/<str:warehouse_slug>",
        view=warehouse_delete_view,
        name="warehouse-delete",
    ),
    path(
        "warehouse/update/<str:warehouse_slug>",
        view=warehouse_update_view,
        name="warehouse-update",
    ),
    path(
        "warehouse/detail/<str:warehouse_slug>/",
        view=warehouse_detail_view,
        name="warehouse-detail",
    ),
    path(
        "warehouse_employee/",
        view=warehouse_employee_list_view,
        name="employee-list",
    ),
    path(
        "warehouse_employee/create/",
        view=warehouse_employee_create_view,
        name="employee-create",
    ),
    path(
        "warehouse_employee/delete/<str:warehouse_slug>/<str:employee_slug>/",
        view=warehouse_employee_delete_view,
        name="employee-delete",
    ),
    path(
        "warehouse_employee/update/<str:warehouse_slug>/<str:employee_slug>/",
        view=warehouse_employee_update_view,
        name="employee-update",
    ),
    path(
        "warehouse_employee/detail/<str:warehouse_slug>/<str:employee_slug>/",
        view=warehouse_employee_detail_view,
        name="employee-detail",
    ),
    path(
        "warehouse_inventory/",
        view=warehouse_inventory_list_view,
        name="inventory-list",
    ),
    path(
        "warehouse_inventory/create/",
        view=warehouse_inventory_create_view,
        name="inventory-create",
    ),
    path(
        "warehouse_inventory/delete/<str:warehouse_slug>/<str:product_slug>/",
        view=warehouse_inventory_delete_view,
        name="inventory-delete",
    ),
    path(
        "warehouse_inventory/update/<str:warehouse_slug>/<str:product_slug>/",
        view=warehouse_inventory_update_view,
        name="inventory-update",
    ),
    path(
        "warehouse_inventory/detail/<str:warehouse_slug>/<str:product_slug>/",
        view=warehouse_inventory_detail_view,
        name="inventory-detail",
    ),
]
