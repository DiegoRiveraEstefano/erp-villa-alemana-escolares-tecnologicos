from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from erp_villa_alemana_escolares_tecnologicos.apps.utils.mixins import ModelContextMixin

from .forms import CustomerCreateForm
from .forms import CustomerUpdateForm
from .models import Customer


class CustomerDetailView(ModelContextMixin, DetailView):
    model = Customer
    template_name = "customers/customer_detail.html"
    slug_field = "pk"
    slug_url_kwarg = "pk"


customer_detail_view = CustomerDetailView.as_view()


class CustomerListView(ModelContextMixin, ListView):
    model = Customer
    template_name = "customers/customer_list.html"

    def get_queryset(self):
        return super().get_queryset()


customer_list_view = CustomerListView.as_view()


class CustomerCreateView(CreateView):
    model = Customer
    template_name = "customers/customer_create.html"
    form_class = CustomerCreateForm


customer_create_view = CustomerCreateView.as_view()


class CustomerUpdateView(UpdateView):
    model = Customer
    template_name = "customers/customer_update.html"
    form_class = CustomerUpdateForm


customer_update_view = CustomerUpdateView.as_view()


class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = "customers/customer_delete.html"


customer_delete_view = CustomerDeleteView.as_view()
