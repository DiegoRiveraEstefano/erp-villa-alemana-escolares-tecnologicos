from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from erp_villa_alemana_escolares_tecnologicos.apps.utils.mixins import ModelContextMixin

from .forms import EmployeeCreateForm
from .forms import EmployeeDeleteForm
from .forms import EmployeeDepartmentCreateForm
from .forms import EmployeeDepartmentDeleteForm
from .forms import EmployeeDepartmentUpdateForm
from .forms import EmployeePositionCreateForm
from .forms import EmployeePositionDeleteForm
from .forms import EmployeePositionUpdateForm
from .forms import EmployeeUpdateForm
from .models import Employee
from .models import EmployeeDepartment
from .models import EmployeePosition


class EmployeeDetailView(ModelContextMixin, PermissionRequiredMixin, DetailView):
    model = Employee
    template_name = "employees/employee_detail.html"
    slug_field = "pk"
    slug_url_kwarg = "pk"
    context_object_name = "employee"
    permission_required = "employees.can_view_employee"
    permission_denied_message = _("permission denied")


employee_detail_view = EmployeeDetailView.as_view()


class EmployeeListView(ModelContextMixin, PermissionRequiredMixin, ListView):
    model = Employee
    template_name = "employees/employee_list.html"
    context_object_name = "employees"
    permission_required = "employees.can_view_employee"
    permission_denied_message = _("permission denied")


employee_list_view = EmployeeListView.as_view()


class EmployeeCreateView(PermissionRequiredMixin, CreateView):
    model = Employee
    template_name = "employees/employee_create.html"
    form_class = EmployeeCreateForm
    success_url = reverse_lazy("employees:employee-list")
    context_object_name = "employee"
    permission_required = "employees.can_add_employee"
    permission_denied_message = _("permission denied")


employee_create_view = EmployeeCreateView.as_view()


class EmployeeUpdateView(PermissionRequiredMixin, UpdateView):
    model = Employee
    template_name = "employees/employee_update.html"
    form_class = EmployeeUpdateForm
    success_url = reverse_lazy("employees:employee-list")
    context_object_name = "employee"
    permission_required = "employees.can_change_employee"
    permission_denied_message = _("permission denied")


employee_update_view = EmployeeUpdateView.as_view()


class EmployeeDeleteView(PermissionRequiredMixin, DeleteView):
    model = Employee
    template_name = "employees/employee_delete.html"
    form_class = EmployeeDeleteForm
    success_url = reverse_lazy("employees:employee-list")
    context_object_name = "employee"
    permission_required = "employees.can_delete_employee"
    permission_denied_message = _("permission denied")


employee_delete_view = EmployeeDeleteView.as_view()


class EmployeeDepartmentDetailView(
    ModelContextMixin,
    PermissionRequiredMixin,
    DetailView,
):
    model = EmployeeDepartment
    template_name = "employees/department_detail.html"
    slug_field = "slug"
    slug_url_kwarg = "department_slug"
    context_object_name = "department"
    permission_required = "employees.can_view_employee_department"
    permission_denied_message = _("permission denied")


employee_department_detail_view = EmployeeDepartmentDetailView.as_view()


class EmployeeDepartmentListView(ModelContextMixin, PermissionRequiredMixin, ListView):
    model = EmployeeDepartment
    template_name = "employees/department_list.html"
    context_object_name = "departments"
    permission_required = "employees.can_view_employee_department"
    permission_denied_message = _("permission denied")


employee_department_list_view = EmployeeDepartmentListView.as_view()


class EmployeeDepartmentCreateView(PermissionRequiredMixin, CreateView):
    model = EmployeeDepartment
    template_name = "employees/department_create.html"
    form_class = EmployeeDepartmentCreateForm
    success_url = reverse_lazy("employees:department-list")
    permission_required = "employees.can_add_employee_department"
    permission_denied_message = _("permission denied")


employee_department_create_view = EmployeeDepartmentCreateView.as_view()


class EmployeeDepartmentUpdateView(PermissionRequiredMixin, UpdateView):
    model = EmployeeDepartment
    template_name = "employees/department_update.html"
    form_class = EmployeeDepartmentUpdateForm
    slug_field = "slug"
    slug_url_kwarg = "department_slug"
    success_url = reverse_lazy("employees:department-list")
    permission_required = "employees.can_change_employee_department"
    permission_denied_message = _("permission denied")


employee_department_update_view = EmployeeDepartmentUpdateView.as_view()


class EmployeeDepartmentDeleteView(PermissionRequiredMixin, DeleteView):
    model = EmployeeDepartment
    template_name = "employees/department_delete.html"
    form_class = EmployeeDepartmentDeleteForm
    slug_field = "slug"
    slug_url_kwarg = "department_slug"
    success_url = reverse_lazy("employees:department-list")
    permission_required = "employees.can_delete_employee_department"
    permission_denied_message = _("permission denied")


employee_department_delete_view = EmployeeDepartmentDeleteView.as_view()


class EmployeePositionDetailView(
    ModelContextMixin,
    PermissionRequiredMixin,
    DetailView,
):
    model = EmployeePosition
    template_name = "employees/position_detail.html"
    slug_field = "slug"
    slug_url_kwarg = "position_slug"
    context_object_name = "position"
    permission_required = "employees.can_view_employee_position"
    permission_denied_message = _("permission denied")


employee_position_detail_view = EmployeePositionDetailView.as_view()


class EmployeePositionListView(ModelContextMixin, PermissionRequiredMixin, ListView):
    model = EmployeePosition
    template_name = "employees/position_list.html"
    context_object_name = "positions"
    permission_required = "employees.can_view_employee_position"
    permission_denied_message = _("permission denied")


employee_position_list_view = EmployeePositionListView.as_view()


class EmployeePositionCreateView(PermissionRequiredMixin, CreateView):
    model = EmployeePosition
    template_name = "employees/position_create.html"
    form_class = EmployeePositionCreateForm
    success_url = reverse_lazy("employees:position-list")
    permission_required = "employees.can_add_employee_position"
    permission_denied_message = _("permission denied")


employee_position_create_view = EmployeePositionCreateView.as_view()


class EmployeePositionUpdateView(PermissionRequiredMixin, UpdateView):
    model = EmployeePosition
    template_name = "employees/position_update.html"
    form_class = EmployeePositionUpdateForm
    slug_field = "slug"
    slug_url_kwarg = "position_slug"
    success_url = reverse_lazy("employees:position-list")
    permission_required = "employees.can_change_employee_position"
    permission_denied_message = _("permission denied")


employee_position_update_view = EmployeePositionUpdateView.as_view()


class EmployeePositionDeleteView(PermissionRequiredMixin, DeleteView):
    model = EmployeePosition
    template_name = "employees/position_delete.html"
    form_class = EmployeePositionDeleteForm
    slug_field = "slug"
    slug_url_kwarg = "position_slug"
    success_url = reverse_lazy("employees:position-list")
    permission_required = "employees.can_delete_employee_position"
    permission_denied_message = _("permission denied")


employee_position_delete_view = EmployeePositionDeleteView.as_view()
