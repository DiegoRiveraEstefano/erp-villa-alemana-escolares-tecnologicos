from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.views import defaults as default_views
from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path(
        "about/",
        TemplateView.as_view(template_name="pages/about.html"),
        name="about",
    ),
    # --- Django JET URLS ---
    path("jet/", include("jet.urls", "jet")),  # Django JET URLS
    path(
        "jet/dashboard/",
        include("jet.dashboard.urls", "jet-dashboard"),
    ),  # Django JET dashboard URLS
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path(
        "users/",
        include(
            "erp_villa_alemana_escolares_tecnologicos.apps.users.urls",
            namespace="users",
        ),
    ),
    path(
        "stores/",
        include(
            "erp_villa_alemana_escolares_tecnologicos.apps.stores.urls",
            namespace="stores",
        ),
    ),
    path(
        "warehouses/",
        include(
            "erp_villa_alemana_escolares_tecnologicos.apps.warehouses.urls",
            namespace="warehouses",
        ),
    ),
    path(
        "products/",
        include(
            "erp_villa_alemana_escolares_tecnologicos.apps.products.urls",
            namespace="products",
        ),
    ),
    path(
        "customers/",
        include(
            "erp_villa_alemana_escolares_tecnologicos.apps.customers.urls",
            namespace="customers",
        ),
    ),
    path(
        "employees/",
        include(
            "erp_villa_alemana_escolares_tecnologicos.apps.employees.urls",
            namespace="employees",
        ),
    ),
    path(
        "sales/",
        include(
            "erp_villa_alemana_escolares_tecnologicos.apps.sales.urls",
            namespace="sales",
        ),
    ),
    path(
        "address/",
        include(
            "erp_villa_alemana_escolares_tecnologicos.apps.addresses.urls",
            namespace="address",
        ),
    ),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]


if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
        path("__reload__/", include("django_browser_reload.urls")),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [
            path("__debug__/", include(debug_toolbar.urls)),
            *urlpatterns,
        ]
