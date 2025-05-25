from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from erp_villa_alemana_escolares_tecnologicos.apps.utils.mixins import ModelContextMixin

from .forms import WarehouseCreateForm
from .forms import WarehouseEmployeeCreateForm
from .forms import WarehouseEmployeeDeleteForm
from .forms import WarehouseEmployeeUpdateForm
from .forms import WarehouseInventoryCreateForm
from .forms import WarehouseInventoryDeleteForm
from .forms import WarehouseInventoryUpdateForm
from .forms import WarehouseUpdateForm
from .models import Warehouse
from .models import WarehouseEmployee
from .models import WarehouseInventory


class WarehouseDetailView(ModelContextMixin, PermissionRequiredMixin, DetailView):
    model = Warehouse
    template_name = "warehouses/warehouse_detail.html"
    slug_field = "slug"
    slug_url_kwarg = "warehouse_slug"
    context_object_name = "warehouse"
    permission_required = "warehouses.can_view_warehouse"
    permission_denied_message = _("permission denied")


warehouse_detail_view = WarehouseDetailView.as_view()


class WarehouseListView(ModelContextMixin, PermissionRequiredMixin, ListView):
    model = Warehouse
    template_name = "warehouses/warehouse_list.html"
    context_object_name = "warehouse"
    permission_required = "warehouses.can_view_warehouse"
    permission_denied_message = _("permission denied")


warehouse_list_view = WarehouseListView.as_view()


class WarehouseCreateView(PermissionRequiredMixin, CreateView):
    model = Warehouse
    template_name = "warehouses/warehouse_create.html"
    form_class = WarehouseCreateForm
    success_url = reverse_lazy("warehouses:warehouse-list")
    context_object_name = "warehouse"
    permission_required = "warehouses.can_add_warehouse"
    permission_denied_message = _("permission denied")


warehouse_create_view = WarehouseCreateView.as_view()


class WarehouseUpdateView(PermissionRequiredMixin, UpdateView):
    model = Warehouse
    template_name = "warehouses/warehouse_update.html"
    form_class = WarehouseUpdateForm
    success_url = reverse_lazy("warehouses:warehouse-list")
    context_object_name = "warehouse"
    slug_field = "slug"
    slug_url_kwarg = "warehouse_slug"
    permission_required = "warehouses.can_edit_warehouse"
    permission_denied_message = _("permission denied")


warehouse_update_view = WarehouseUpdateView.as_view()


class WarehouseDeleteView(PermissionRequiredMixin, DeleteView):
    model = Warehouse
    template_name = "warehouses/warehouse_delete.html"
    success_url = reverse_lazy("warehouse:warehouse-list")
    context_object_name = "warehouse"
    slug_field = "slug"
    slug_url_kwarg = "warehouse_slug"
    permission_required = "warehouses.can_delete_warehouse"
    permission_denied_message = _("permission denied")


warehouse_delete_view = WarehouseDeleteView.as_view()


class WarehouseEmployeeDetailView(
    ModelContextMixin,
    PermissionRequiredMixin,
    DetailView,
):
    model = WarehouseEmployee
    template_name = "warehouses/employee_detail.html"
    slug_field = "pk"
    slug_url_kwarg = "pk"
    context_object_name = "warehouse_employee"
    permission_required = "warehouses.can_view_warehouse_employee"
    permission_denied_message = _("permission denied")


warehouse_employee_detail_view = WarehouseEmployeeDetailView.as_view()


class WarehouseEmployeeListView(ModelContextMixin, PermissionRequiredMixin, ListView):
    model = WarehouseEmployee
    template_name = "warehouses/employee_list.html"
    context_object_name = "warehouse_employee"
    permission_required = "warehouses.can_view_warehouse_employee"
    permission_denied_message = _("permission denied")


warehouse_employee_list_view = WarehouseEmployeeListView.as_view()


class WarehouseEmployeeCreateView(PermissionRequiredMixin, CreateView):
    model = WarehouseEmployee
    template_name = "warehouses/employee_create.html"
    form_class = WarehouseEmployeeCreateForm
    success_url = reverse_lazy("warehouses:employee-list")
    context_object_name = "warehouse_employee"
    permission_required = "warehouses.can_add_warehouse_employee"
    permission_denied_message = _("permission denied")


warehouse_employee_create_view = WarehouseEmployeeCreateView.as_view()


class WarehouseEmployeeUpdateView(PermissionRequiredMixin, UpdateView):
    model = WarehouseEmployee
    template_name = "warehouses/employee_update.html"
    form_class = WarehouseEmployeeUpdateForm
    success_url = reverse_lazy("warehouses:employee-list")
    context_object_name = "warehouse_employee"
    slug_field = "pk"
    slug_url_kwarg = "pk"
    permission_required = "warehouses.can_edit_warehouse_employee"
    permission_denied_message = _("permission denied")


warehouse_employee_update_view = WarehouseEmployeeUpdateView.as_view()


class WarehouseEmployeeDeleteView(PermissionRequiredMixin, DeleteView):
    model = WarehouseEmployee
    form_class = WarehouseEmployeeDeleteForm
    template_name = "warehouses/employee_delete.html"
    success_url = reverse_lazy("warehouses:employee-list")
    context_object_name = "warehouse_employee"
    slug_field = "pk"
    slug_url_kwarg = "pk"
    permission_required = "warehouses.can_delete_warehouse_employee"
    permission_denied_message = _("permission denied")


warehouse_employee_delete_view = WarehouseEmployeeDeleteView.as_view()


class WarehouseInventoryDetailView(
    ModelContextMixin,
    PermissionRequiredMixin,
    DetailView,
):
    model = WarehouseInventory
    template_name = "warehouses/inventory_detail.html"
    slug_field = "pk"
    slug_url_kwarg = "pk"
    context_object_name = "warehouse_inventory"
    permission_required = "warehouses.can_view_warehouse_inventory"
    permission_denied_message = _("permission denied")


warehouse_inventory_detail_view = WarehouseInventoryDetailView.as_view()


class WarehouseInventoryListView(ModelContextMixin, PermissionRequiredMixin, ListView):
    model = WarehouseInventory
    template_name = "warehouses/inventory_list.html"
    context_object_name = "warehouse_inventory"
    permission_required = "warehouses.can_view_warehouse_inventory"
    permission_denied_message = _("permission denied")


warehouse_inventory_list_view = WarehouseInventoryListView.as_view()


class WarehouseInventoryCreateView(PermissionRequiredMixin, CreateView):
    model = WarehouseInventory
    template_name = "warehouses/inventory_create.html"
    form_class = WarehouseInventoryCreateForm
    success_url = reverse_lazy("warehouses:inventory-list")
    context_object_name = "warehouse_inventory"
    permission_required = "warehouses.can_add_warehouse_inventory"
    permission_denied_message = _("permission denied")


warehouse_inventory_create_view = WarehouseInventoryCreateView.as_view()


class WarehouseInventoryUpdateView(PermissionRequiredMixin, UpdateView):
    model = WarehouseInventory
    template_name = "warehouses/inventory_update.html"
    form_class = WarehouseInventoryUpdateForm
    success_url = reverse_lazy("warehouses:inventory-list")
    context_object_name = "warehouse_inventory"
    slug_field = "pk"
    slug_url_kwarg = "pk"
    permission_required = "warehouses.can_edit_warehouse_inventory"
    permission_denied_message = _("permission denied")


warehouse_inventory_update_view = WarehouseInventoryUpdateView.as_view()


class WarehouseInventoryDeleteView(PermissionRequiredMixin, DeleteView):
    model = WarehouseInventory
    form_class = WarehouseInventoryDeleteForm
    template_name = "warehouses/inventory_delete.html"
    success_url = reverse_lazy("warehouses:inventory-list")
    context_object_name = "warehouse_inventory"
    slug_field = "pk"
    slug_url_kwarg = "pk"
    permission_required = "warehouses.can_delete_warehouse_inventory"
    permission_denied_message = _("permission denied")


warehouse_inventory_delete_view = WarehouseInventoryDeleteView.as_view()
