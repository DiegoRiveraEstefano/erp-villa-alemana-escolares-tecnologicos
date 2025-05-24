from django.urls import reverse_lazy
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


class StoreDetailView(ModelContextMixin, DetailView):
    model = Store
    template_name = "stores/store_detail.html"
    slug_field = "pk"
    slug_url_kwarg = "pk"
    context_object_name = "store"


store_detail_view = StoreDetailView.as_view()


class StoreListView(ModelContextMixin, ListView):
    model = Store
    template_name = "stores/store_list.html"
    context_object_name = "store"

    def get_queryset(self):
        return super().get_queryset()


store_list_view = StoreListView.as_view()


class StoreCreateView(CreateView):
    model = Store
    template_name = "stores/store_create.html"
    form_class = StoreCreateForm
    success_url = reverse_lazy("store:store-list")
    context_object_name = "store"


store_create_view = StoreCreateView.as_view()


class StoreUpdateView(UpdateView):
    model = Store
    template_name = "stores/store_update.html"
    form_class = StoreUpdateForm
    success_url = reverse_lazy("store:store-list")
    context_object_name = "store"


store_update_view = StoreUpdateView.as_view()


class StoreDeleteView(DeleteView):
    model = Store
    template_name = "stores/store_delete.html"
    success_url = reverse_lazy("store:store-list")
    context_object_name = "store"


store_delete_view = StoreDeleteView.as_view()


class StoreEmployeeDetailView(ModelContextMixin, DetailView):
    model = StoreEmployee
    template_name = "stores/employee_detail.html"
    slug_field = "pk"
    slug_url_kwarg = "pk"
    context_object_name = "store_employee"


store_employee_detail_view = StoreEmployeeDetailView.as_view()


class StoreEmployeeListView(ModelContextMixin, ListView):
    model = StoreEmployee
    template_name = "stores/employee_list.html"
    context_object_name = "store_employee"

    def get_queryset(self):
        return super().get_queryset()


store_employee_list_view = StoreEmployeeListView.as_view()


class StoreEmployeeCreateView(CreateView):
    model = StoreEmployee
    template_name = "stores/employee_create.html"
    form_class = StoreEmployeeCreateForm
    success_url = reverse_lazy("stores:employee-list")
    context_object_name = "store_employee"


store_employee_create_view = StoreEmployeeCreateView.as_view()


class StoreEmployeeUpdateView(UpdateView):
    model = StoreEmployee
    template_name = "stores/employee_update.html"
    form_class = StoreEmployeeUpdateForm
    success_url = reverse_lazy("stores:employee-list")
    context_object_name = "store_employee"


store_employee_update_view = StoreEmployeeUpdateView.as_view()


class StoreEmployeeDeleteView(DeleteView):
    model = StoreEmployee
    template_name = "stores/employee_delete.html"
    success_url = reverse_lazy("stores:employee-list")
    context_object_name = "store_employee"


store_employee_delete_view = StoreEmployeeDeleteView.as_view()
