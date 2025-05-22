from django.urls import path

from .views import employee_create_view
from .views import employee_delete_view
from .views import employee_department_create_view
from .views import employee_department_delete_view
from .views import employee_department_detail_view
from .views import employee_department_list_view
from .views import employee_department_update_view
from .views import employee_detail_view
from .views import employee_list_view
from .views import employee_position_create_view
from .views import employee_position_delete_view
from .views import employee_position_detail_view
from .views import employee_position_list_view
from .views import employee_position_update_view
from .views import employee_update_view

app_name = "employees"
urlpatterns = [
    path("employee/", view=employee_list_view, name="employee-list"),
    path("employee/create/", view=employee_create_view, name="employee-create"),
    path("employee/delete/<str:pk>", view=employee_delete_view, name="employee-delete"),
    path("employee/update/<str:pk>", view=employee_update_view, name="employee-update"),
    path(
        "employee/detail/<str:pk>/",
        view=employee_detail_view,
        name="employee-detail",
    ),
    path(
        "employee_department/",
        view=employee_department_list_view,
        name="department-list",
    ),
    path(
        "employee_department/create/",
        view=employee_department_create_view,
        name="department-create",
    ),
    path(
        "employee_department/delete/<str:department_slug>",
        view=employee_department_delete_view,
        name="department-delete",
    ),
    path(
        "employee_department/update/<str:department_slug>",
        view=employee_department_update_view,
        name="department-update",
    ),
    path(
        "employee_department/detail/<str:department_slug>/",
        view=employee_department_detail_view,
        name="department-detail",
    ),
    path(
        "employee_position/",
        view=employee_position_list_view,
        name="position-list",
    ),
    path(
        "employee_position/create/",
        view=employee_position_create_view,
        name="position-create",
    ),
    path(
        "employee_position/delete/<str:position_slug>",
        view=employee_position_delete_view,
        name="position-delete",
    ),
    path(
        "employee_position/update/<str:position_slug>",
        view=employee_position_update_view,
        name="position-update",
    ),
    path(
        "employee_position/detail/<str:position_slug>/",
        view=employee_position_detail_view,
        name="position-detail",
    ),
]
