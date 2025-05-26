from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from erp_villa_alemana_escolares_tecnologicos.apps.utils.mixins import ModelContextMixin

from .forms import StoreCreateForm
from .forms import StoreEmployeeCreateForm
from .forms import StoreEmployeeUpdateForm
from .forms import StoreUpdateForm
from .models import Store
from .models import StoreEmployee


class StoreDetailView(ModelContextMixin, PermissionRequiredMixin, DetailView):
    model = Store
    template_name = "stores/store_detail.html"
    slug_field = "slug"
    slug_url_kwarg = "store_slug"
    context_object_name = "store"
    permission_required = "stores.can_view_store"
    permission_denied_message = _("permission denied")


store_detail_view = StoreDetailView.as_view()


class StoreListView(ModelContextMixin, PermissionRequiredMixin, ListView):
    model = Store
    template_name = "stores/store_list.html"
    context_object_name = "store"
    permission_required = "stores.can_view_store"
    permission_denied_message = _("permission denied")


store_list_view = StoreListView.as_view()


class StoreCreateView(PermissionRequiredMixin, CreateView):
    model = Store
    template_name = "stores/store_create.html"
    form_class = StoreCreateForm
    success_url = reverse_lazy("stores:store-list")
    context_object_name = "store"
    permission_required = "stores.can_add_store"
    permission_denied_message = _("permission denied")


store_create_view = StoreCreateView.as_view()


class StoreUpdateView(PermissionRequiredMixin, UpdateView):
    model = Store
    template_name = "stores/store_update.html"
    form_class = StoreUpdateForm
    success_url = reverse_lazy("stores:store-list")
    context_object_name = "store"
    slug_field = "slug"
    slug_url_kwarg = "store_slug"
    permission_required = "stores.can_edit_store"
    permission_denied_message = _("permission denied")


store_update_view = StoreUpdateView.as_view()


class StoreDeleteView(PermissionRequiredMixin, DeleteView):
    model = Store
    template_name = "stores/store_delete.html"
    success_url = reverse_lazy("stores:store-list")
    context_object_name = "store"
    slug_field = "slug"
    slug_url_kwarg = "store_slug"
    permission_required = "stores.can_delete_store"
    permission_denied_message = _("permission denied")


store_delete_view = StoreDeleteView.as_view()


class StoreEmployeeDetailView(ModelContextMixin, PermissionRequiredMixin, DetailView):
    model = StoreEmployee
    template_name = "stores/employee_detail.html"
    slug_field = "pk"
    slug_url_kwarg = "pk"
    context_object_name = "store_employee"
    permission_required = "stores.can_view_store_employee"
    permission_denied_message = _("permission denied")


store_employee_detail_view = StoreEmployeeDetailView.as_view()


class StoreEmployeeListView(ModelContextMixin, PermissionRequiredMixin, ListView):
    model = StoreEmployee
    template_name = "stores/employee_list.html"
    context_object_name = "store_employee"
    permission_required = "stores.can_view_store_employee"
    permission_denied_message = _("permission denied")


store_employee_list_view = StoreEmployeeListView.as_view()


class StoreEmployeeCreateView(PermissionRequiredMixin, CreateView):
    model = StoreEmployee
    template_name = "stores/employee_create.html"
    form_class = StoreEmployeeCreateForm
    success_url = reverse_lazy("stores:employee-list")
    context_object_name = "store_employee"
    permission_required = "stores.can_add_store_employee"
    permission_denied_message = _("permission denied")


store_employee_create_view = StoreEmployeeCreateView.as_view()


class StoreEmployeeUpdateView(PermissionRequiredMixin, UpdateView):
    model = StoreEmployee
    template_name = "stores/employee_update.html"
    form_class = StoreEmployeeUpdateForm
    success_url = reverse_lazy("stores:employee-list")
    context_object_name = "store_employee"
    slug_field = "pk"
    slug_url_kwarg = "pk"
    permission_required = "stores.can_edit_store_employee"
    permission_denied_message = _("permission denied")


store_employee_update_view = StoreEmployeeUpdateView.as_view()


class StoreEmployeeDeleteView(PermissionRequiredMixin, DeleteView):
    model = StoreEmployee
    template_name = "stores/employee_delete.html"
    success_url = reverse_lazy("stores:employee-list")
    context_object_name = "store_employee"
    slug_field = "pk"
    slug_url_kwarg = "pk"
    permission_required = "stores.can_delete_store_employee"
    permission_denied_message = _("permission denied")


store_employee_delete_view = StoreEmployeeDeleteView.as_view()
