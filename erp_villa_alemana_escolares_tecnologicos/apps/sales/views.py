from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from erp_villa_alemana_escolares_tecnologicos.apps.utils.mixins import ModelContextMixin

from .forms import SaleCreateForm
from .forms import SaleDeleteForm
from .forms import SaleUpdateForm
from .models import Sale


class SaleDetailView(ModelContextMixin, PermissionRequiredMixin, DetailView):
    model = Sale
    template_name = "sales/sale_detail.html"
    slug_field = "pk"
    slug_url_kwarg = "pk"
    context_object_name = "sale"
    permission_required = "sales.can_view_sale"
    permission_denied_message = _("permission denied")


sale_detail_view = SaleDetailView.as_view()


class SaleListView(ModelContextMixin, PermissionRequiredMixin, ListView):
    model = Sale
    template_name = "sales/sale_list.html"
    context_object_name = "sale"
    permission_required = "sales.can_view_sale"
    permission_denied_message = _("permission denied")


sale_list_view = SaleListView.as_view()


class SaleCreateView(PermissionRequiredMixin, CreateView):
    model = Sale
    template_name = "sales/sale_create.html"
    form_class = SaleCreateForm
    success_url = reverse_lazy("sale:sale-list")
    context_object_name = "sale"
    permission_required = "sales.can_add_sale"
    permission_denied_message = _("permission denied")


sale_create_view = SaleCreateView.as_view()


class SaleUpdateView(PermissionRequiredMixin, UpdateView):
    model = Sale
    template_name = "sales/sale_update.html"
    form_class = SaleUpdateForm
    success_url = reverse_lazy("sale:sale-list")
    context_object_name = "sale"
    permission_required = "sales.can_change_sale"
    permission_denied_message = _("permission denied")


sale_update_view = SaleUpdateView.as_view()


class SaleDeleteView(PermissionRequiredMixin, DeleteView):
    model = Sale
    form_class = SaleDeleteForm
    template_name = "sales/sale_delete.html"
    success_url = reverse_lazy("sale:sale-list")
    context_object_name = "sale"
    permission_required = "sales.can_delete_sale"
    permission_denied_message = _("permission denied")


sale_delete_view = SaleDeleteView.as_view()
