from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from erp_villa_alemana_escolares_tecnologicos.apps.utils.mixins import ModelContextMixin

from .forms import AddressCreateForm
from .forms import AddressUpdateForm
from .models import Address


class AddressDetailView(ModelContextMixin, PermissionRequiredMixin, DetailView):
    model = Address
    template_name = "address/address_detail.html"
    slug_field = "pk"
    slug_url_kwarg = "pk"
    context_object_name = "address"
    permission_required = "address.can_view_address"
    permission_denied_message = _("permission denied")


address_detail_view = AddressDetailView.as_view()


class AddressListView(ModelContextMixin, PermissionRequiredMixin, ListView):
    model = Address
    template_name = "address/address_list.html"
    context_object_name = "address"
    permission_required = "address.can_view_address"
    permission_denied_message = _("permission denied")


address_list_view = AddressListView.as_view()


class AddressCreateView(PermissionRequiredMixin, CreateView):
    model = Address
    template_name = "address/address_create.html"
    form_class = AddressCreateForm
    success_url = reverse_lazy("address:address-list")
    context_object_name = "address"
    permission_required = "address.can_add_address"
    permission_denied_message = _("permission denied")


address_create_view = AddressCreateView.as_view()


class AddressUpdateView(PermissionRequiredMixin, UpdateView):
    model = Address
    template_name = "address/address_update.html"
    form_class = AddressUpdateForm
    success_url = reverse_lazy("address:address-list")
    context_object_name = "address"
    permission_required = "address.can_edit_address"
    permission_denied_message = _("permission denied")


address_update_view = AddressUpdateView.as_view()


class AddressDeleteView(PermissionRequiredMixin, DeleteView):
    model = Address
    template_name = "address/address_delete.html"
    success_url = reverse_lazy("address:address-list")
    context_object_name = "address"
    permission_required = "address.can_edit_address"
    permission_denied_message = _("permission denied")


address_delete_view = AddressDeleteView.as_view()
