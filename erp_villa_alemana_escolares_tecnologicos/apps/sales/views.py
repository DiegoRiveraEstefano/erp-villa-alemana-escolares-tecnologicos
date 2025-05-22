from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from .forms import SaleCreateForm
from .forms import SaleUpdateForm
from .models import Sale


class SaleDetailView(DetailView):
    model = Sale
    template_name = "sales/sale_detail.html"
    slug_field = "pk"
    slug_url_kwarg = "pk"
    context_object_name = "sale"


sale_detail_view = SaleDetailView.as_view()


class SaleListView(ListView):
    model = Sale
    template_name = "sales/sale_list.html"
    context_object_name = "sale"

    def get_queryset(self):
        return super().get_queryset()


sale_list_view = SaleListView.as_view()


class SaleCreateView(CreateView):
    model = Sale
    template_name = "sales/sale_create.html"
    form_class = SaleCreateForm
    success_url = reverse_lazy("sale:sale-list")
    context_object_name = "sale"


sale_create_view = SaleCreateView.as_view()


class SaleUpdateView(UpdateView):
    model = Sale
    template_name = "sales/sale_update.html"
    form_class = SaleUpdateForm
    success_url = reverse_lazy("sale:sale-list")
    context_object_name = "sale"


sale_update_view = SaleUpdateView.as_view()


class SaleDeleteView(DeleteView):
    model = Sale
    template_name = "sales/sale_delete.html"
    success_url = reverse_lazy("sale:sale-list")
    context_object_name = "sale"


sale_delete_view = SaleDeleteView.as_view()
