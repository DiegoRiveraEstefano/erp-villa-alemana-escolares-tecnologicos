from django.urls import path

from .views import audit_detail_view
from .views import audit_list_view

app_name = "audits"
urlpatterns = [
    path("", view=audit_list_view, name="list"),
    path("<int:pk>/", view=audit_detail_view, name="detail"),
]
