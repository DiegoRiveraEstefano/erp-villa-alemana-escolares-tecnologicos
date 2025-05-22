from django.urls import path

from .views import user_detail_view
from .views import user_group_detail_view
from .views import user_group_list_view
from .views import user_log_out_view
from .views import user_login_view
from .views import user_redirect_view
from .views import user_update_view

app_name = "users"
urlpatterns = [
    path("redirect/", view=user_redirect_view, name="redirect"),
    path("update/", view=user_update_view, name="update"),
    path("login/", view=user_login_view, name="login"),
    path("logout/", view=user_log_out_view, name="logout"),
    path("me/", view=user_detail_view, name="me"),
    path("<str:username>/", view=user_detail_view, name="detail"),
    path("groups/", view=user_group_list_view, name="group-list"),
    path("groups/<str:slug>/", view=user_group_detail_view, name="group-detail"),
]
