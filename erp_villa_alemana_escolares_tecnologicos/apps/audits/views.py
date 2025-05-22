from auditlog.models import LogEntry
from django.core.paginator import Paginator
from django.views.generic import DetailView
from django.views.generic import ListView

from erp_villa_alemana_escolares_tecnologicos.apps.utils.mixins import ModelContextMixin


class AuditListView(ModelContextMixin, ListView):
    model = LogEntry
    template_name = "audits/audit_list.html"
    context_object_name = "audits"
    paginate_by = 10
    paginator_class = Paginator


audit_list_view = AuditListView.as_view()


class AuditDetailView(DetailView):
    model = LogEntry
    template_name = "audits/audit_detail.html"
    context_object_name = "audit"


audit_detail_view = AuditDetailView.as_view()
