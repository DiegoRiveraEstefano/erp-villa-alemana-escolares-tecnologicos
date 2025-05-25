from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from erp_villa_alemana_escolares_tecnologicos.apps.utils.mixins import ModelContextMixin

from .forms import CustomerCreateForm
from .forms import CustomerUpdateForm
from .models import Customer


class CustomerDetailView(ModelContextMixin, PermissionRequiredMixin, DetailView):
    model = Customer
    template_name = "customers/customer_detail.html"
    slug_field = "pk"
    slug_url_kwarg = "pk"
    context_object_name = "customer"
    permission_required = "customers.can_view_customer"
    permission_denied_message = _("permission denied")


customer_detail_view = CustomerDetailView.as_view()


class CustomerListView(ModelContextMixin, PermissionRequiredMixin, ListView):
    model = Customer
    template_name = "customers/customer_list.html"
    context_object_name = "customers"
    permission_required = "customers.can_view_customer"
    permission_denied_message = _("permission denied")


customer_list_view = CustomerListView.as_view()


class CustomerCreateView(PermissionRequiredMixin, CreateView):
    model = Customer
    template_name = "customers/customer_create.html"
    form_class = CustomerCreateForm
    success_url = reverse_lazy("customers:customer-list")
    context_object_name = "customer"
    permission_required = "customers.can_add_customer"


customer_create_view = CustomerCreateView.as_view()


class CustomerUpdateView(PermissionRequiredMixin, UpdateView):
    model = Customer
    template_name = "customers/customer_update.html"
    form_class = CustomerUpdateForm
    success_url = reverse_lazy("customers:customer-list")
    context_object_name = "customer"
    permission_required = "customers.can_change_customer"
    permission_denied_message = _("permission denied")


customer_update_view = CustomerUpdateView.as_view()


class CustomerDeleteView(PermissionRequiredMixin, DeleteView):
    model = Customer
    template_name = "customers/customer_delete.html"
    success_url = reverse_lazy("customers:customer-list")
    context_object_name = "customer"
    permission_required = "customers.can_delete_customer"
    permission_denied_message = _("permission denied")


customer_delete_view = CustomerDeleteView.as_view()
