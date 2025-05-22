from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from .forms import AddressCreateForm
from .forms import AddressUpdateForm
from .models import Address


class AddressDetailView(DetailView):
    model = Address
    template_name = "address/address_detail.html"
    slug_field = "pk"
    slug_url_kwarg = "pk"
    context_object_name = "address"


address_detail_view = AddressDetailView.as_view()


class AddressListView(ListView):
    model = Address
    template_name = "address/address_list.html"
    context_object_name = "address"

    def get_queryset(self):
        return super().get_queryset()


address_list_view = AddressListView.as_view()


class AddressCreateView(CreateView):
    model = Address
    template_name = "address/address_create.html"
    form_class = AddressCreateForm
    success_url = reverse_lazy("address:address-list")
    context_object_name = "address"


address_create_view = AddressCreateView.as_view()


class AddressUpdateView(UpdateView):
    model = Address
    template_name = "address/address_update.html"
    form_class = AddressUpdateForm
    success_url = reverse_lazy("address:address-list")
    context_object_name = "address"


address_update_view = AddressUpdateView.as_view()


class AddressDeleteView(DeleteView):
    model = Address
    template_name = "address/address_delete.html"
    success_url = reverse_lazy("address:address-list")
    context_object_name = "address"


address_delete_view = AddressDeleteView.as_view()
