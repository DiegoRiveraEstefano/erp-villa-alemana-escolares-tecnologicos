from django.urls import path

from .views import store_create_view
from .views import store_delete_view
from .views import store_detail_view
from .views import store_employee_create_view
from .views import store_employee_delete_view
from .views import store_employee_detail_view
from .views import store_employee_list_view
from .views import store_list_view
from .views import store_update_view

app_name = "stores"
urlpatterns = [
    path("store/", view=store_list_view, name="store-list"),
    path("store/create/", view=store_create_view, name="store-create"),
    path("store/delete/<str:store_slug>", view=store_delete_view, name="store-delete"),
    path("store/update/<str:store_slug>", view=store_update_view, name="store-update"),
    path(
        "store/detail/<str:store_slug>/",
        view=store_detail_view,
        name="store-detail",
    ),
    path(
        "employee/",
        view=store_employee_list_view,
        name="employee-list",
    ),
    path(
        "employee/create/",
        view=store_employee_create_view,
        name="employee-create",
    ),
    path(
        "employee/delete/<int:pk>",
        view=store_employee_delete_view,
        name="employee-delete",
    ),
    path(
        "employee/detail/<int:pk>/",
        view=store_employee_detail_view,
        name="employee-detail",
    ),
]
