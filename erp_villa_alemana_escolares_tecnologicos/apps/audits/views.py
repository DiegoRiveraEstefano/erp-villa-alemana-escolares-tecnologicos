from auditlog.models import LogEntry
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.paginator import Paginator
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView
from django.views.generic import ListView

from erp_villa_alemana_escolares_tecnologicos.apps.utils.mixins import ModelContextMixin


class AuditListView(ModelContextMixin, PermissionRequiredMixin, ListView):
    model = LogEntry
    template_name = "audits/audit_list.html"
    context_object_name = "audits"
    paginate_by = 10
    paginator_class = Paginator
    permission_required = "auditlog.can_view_audit"
    permission_denied_message = _("permission denied")


audit_list_view = AuditListView.as_view()


class AuditDetailView(ModelContextMixin, PermissionRequiredMixin, DetailView):
    model = LogEntry
    template_name = "audits/audit_detail.html"
    context_object_name = "audit"
    slug_field = "pk"
    slug_url_kwarg = "pk"
    permission_required = "auditlog.can_view_audit"
    permission_denied_message = _("permission denied")


audit_detail_view = AuditDetailView.as_view()
