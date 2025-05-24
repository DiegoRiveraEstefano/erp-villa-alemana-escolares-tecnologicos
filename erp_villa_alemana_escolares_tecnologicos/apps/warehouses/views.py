from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from erp_villa_alemana_escolares_tecnologicos.apps.utils.mixins import ModelContextMixin

from .forms import WarehouseCreateForm
from .forms import WarehouseEmployeeCreateForm
from .forms import WarehouseEmployeeUpdateForm
from .forms import WarehouseInventoryCreateForm
from .forms import WarehouseInventoryUpdateForm
from .forms import WarehouseUpdateForm
from .models import Warehouse
from .models import WarehouseEmployee
from .models import WarehouseInventory


class WarehouseDetailView(ModelContextMixin, DetailView):
    model = Warehouse
    template_name = "warehouse/warehouse_detail.html"
    slug_field = "pk"
    slug_url_kwarg = "pk"
    context_object_name = "warehouse"


warehouse_detail_view = WarehouseDetailView.as_view()


class WarehouseListView(ModelContextMixin, ListView):
    model = Warehouse
    template_name = "warehouse/warehouse_list.html"
    context_object_name = "warehouse"

    def get_queryset(self):
        return super().get_queryset()


warehouse_list_view = WarehouseListView.as_view()


class WarehouseCreateView(CreateView):
    model = Warehouse
    template_name = "warehouse/warehouse_create.html"
    form_class = WarehouseCreateForm
    success_url = reverse_lazy("warehouse:warehouse-list")
    context_object_name = "warehouse"


warehouse_create_view = WarehouseCreateView.as_view()


class WarehouseUpdateView(UpdateView):
    model = Warehouse
    template_name = "warehouse/warehouse_update.html"
    form_class = WarehouseUpdateForm
    success_url = reverse_lazy("warehouse:warehouse-list")
    context_object_name = "warehouse"


warehouse_update_view = WarehouseUpdateView.as_view()


class WarehouseDeleteView(DeleteView):
    model = Warehouse
    template_name = "warehouse/warehouse_delete.html"
    success_url = reverse_lazy("warehouse:warehouse-list")
    context_object_name = "warehouse"


warehouse_delete_view = WarehouseDeleteView.as_view()


class WarehouseEmployeeDetailView(ModelContextMixin, DetailView):
    model = WarehouseEmployee
    template_name = "warehouses/employee_detail.html"
    slug_field = "pk"
    slug_url_kwarg = "pk"
    context_object_name = "warehouse_employee"


warehouse_employee_detail_view = WarehouseEmployeeDetailView.as_view()


class WarehouseEmployeeListView(ModelContextMixin, ListView):
    model = WarehouseEmployee
    template_name = "warehouses/employee_list.html"
    context_object_name = "warehouse_employee"

    def get_queryset(self):
        return super().get_queryset()


warehouse_employee_list_view = WarehouseEmployeeListView.as_view()


class WarehouseEmployeeCreateView(CreateView):
    model = WarehouseEmployee
    template_name = "warehouses/employee_create.html"
    form_class = WarehouseEmployeeCreateForm
    success_url = reverse_lazy("warehouses:employee-list")
    context_object_name = "warehouse_employee"


warehouse_employee_create_view = WarehouseEmployeeCreateView.as_view()


class WarehouseEmployeeUpdateView(UpdateView):
    model = WarehouseEmployee
    template_name = "warehouses/employee_update.html"
    form_class = WarehouseEmployeeUpdateForm
    success_url = reverse_lazy("warehouses:employee-list")
    context_object_name = "warehouse_employee"


warehouse_employee_update_view = WarehouseEmployeeUpdateView.as_view()


class WarehouseEmployeeDeleteView(DeleteView):
    model = WarehouseEmployee
    template_name = "warehouses/employee_delete.html"
    success_url = reverse_lazy("warehouses:employee-list")
    context_object_name = "warehouse_employee"


warehouse_employee_delete_view = WarehouseEmployeeDeleteView.as_view()


class WarehouseInventoryDetailView(ModelContextMixin, DetailView):
    model = WarehouseInventory
    template_name = "warehouses/inventory_detail.html"
    slug_field = "pk"
    slug_url_kwarg = "pk"
    context_object_name = "warehouse_inventory"


warehouse_inventory_detail_view = WarehouseInventoryDetailView.as_view()


class WarehouseInventoryListView(ModelContextMixin, ListView):
    model = WarehouseInventory
    template_name = "warehouses/inventory_list.html"
    context_object_name = "warehouse_inventory"

    def get_queryset(self):
        return super().get_queryset()


warehouse_inventory_list_view = WarehouseInventoryListView.as_view()


class WarehouseInventoryCreateView(CreateView):
    model = WarehouseInventory
    template_name = "warehouses/inventory_create.html"
    form_class = WarehouseInventoryCreateForm
    success_url = reverse_lazy("warehouses:inventory-list")
    context_object_name = "warehouse_inventory"


warehouse_inventory_create_view = WarehouseInventoryCreateView.as_view()


class WarehouseInventoryUpdateView(UpdateView):
    model = WarehouseInventory
    template_name = "warehouses/inventory_update.html"
    form_class = WarehouseInventoryUpdateForm
    success_url = reverse_lazy("warehouses:inventory-list")
    context_object_name = "warehouse_inventory"


warehouse_inventory_update_view = WarehouseInventoryUpdateView.as_view()


class WarehouseInventoryDeleteView(DeleteView):
    model = WarehouseInventory
    template_name = "warehouses/inventory_delete.html"
    success_url = reverse_lazy("warehouses:inventory-list")
    context_object_name = "warehouse_inventory"


warehouse_inventory_delete_view = WarehouseInventoryDeleteView.as_view()
