from django.urls import path

from .views import address_create_view
from .views import address_delete_view
from .views import address_detail_view
from .views import address_list_view
from .views import address_update_view

app_name = "address"
urlpatterns = [
    path("", address_list_view, name="address-list"),
    path("create/", address_create_view, name="address-create"),
    path("<int:pk>/", address_detail_view, name="address-detail"),
    path("<int:pk>/update/", address_update_view, name="address-update"),
    path("<int:pk>/delete/", address_delete_view, name="address-delete"),
]
