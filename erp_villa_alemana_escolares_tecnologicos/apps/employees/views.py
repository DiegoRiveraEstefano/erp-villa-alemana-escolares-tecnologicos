from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from .forms import EmployeeCreateForm
from .forms import EmployeeDepartmentCreateForm
from .forms import EmployeeDepartmentUpdateForm
from .forms import EmployeePositionCreateForm
from .forms import EmployeePositionUpdateForm
from .forms import EmployeeUpdateForm
from .models import Employee
from .models import EmployeeDepartment
from .models import EmployeePosition


class EmployeeDetailView(DetailView):
    model = Employee
    template_name = "employees/employee_detail.html"
    slug_field = "pk"
    slug_url_kwarg = "pk"


employee_detail_view = EmployeeDetailView.as_view()


class EmployeeListView(ListView):
    model = Employee
    template_name = "employees/employee_list.html"

    def get_queryset(self):
        return super().get_queryset()


employee_list_view = EmployeeListView.as_view()


class EmployeeCreateView(CreateView):
    model = Employee
    template_name = "employees/employee_create.html"
    form_class = EmployeeCreateForm


employee_create_view = EmployeeCreateView.as_view()


class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = "employees/employee_update.html"
    form_class = EmployeeUpdateForm


employee_update_view = EmployeeUpdateView.as_view()


class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = "employees/employee_delete.html"


employee_delete_view = EmployeeDeleteView.as_view()


class EmployeeDepartmentDetailView(DetailView):
    model = EmployeeDepartment
    template_name = "employees/department_detail.html"
    slug_field = "pk"
    slug_url_kwarg = "pk"


employee_department_detail_view = EmployeeDepartmentDetailView.as_view()


class EmployeeDepartmentListView(ListView):
    model = EmployeeDepartment
    template_name = "employees/department_list.html"

    def get_queryset(self):
        return super().get_queryset()


employee_department_list_view = EmployeeDepartmentListView.as_view()


class EmployeeDepartmentCreateView(CreateView):
    model = EmployeeDepartment
    template_name = "employees/department_create.html"
    form_class = EmployeeDepartmentCreateForm


employee_department_create_view = EmployeeDepartmentCreateView.as_view()


class EmployeeDepartmentUpdateView(UpdateView):
    model = EmployeeDepartment
    template_name = "employees/department_update.html"
    form_class = EmployeeDepartmentUpdateForm


employee_department_update_view = EmployeeDepartmentUpdateView.as_view()


class EmployeeDepartmentDeleteView(DeleteView):
    model = EmployeeDepartment
    template_name = "employees/department_delete.html"


employee_department_delete_view = EmployeeDepartmentDeleteView.as_view()


class EmployeePositionDetailView(DetailView):
    model = EmployeePosition
    template_name = "employee/position_detail.html"
    slug_field = "pk"
    slug_url_kwarg = "pk"


employee_position_detail_view = EmployeePositionDetailView.as_view()


class EmployeePositionListView(ListView):
    model = EmployeePosition
    template_name = "employee/position_list.html"

    def get_queryset(self):
        return super().get_queryset()


employee_position_list_view = EmployeePositionListView.as_view()


class EmployeePositionCreateView(CreateView):
    model = EmployeePosition
    template_name = "employee/position_create.html"
    form_class = EmployeePositionCreateForm


employee_position_create_view = EmployeePositionCreateView.as_view()


class EmployeePositionUpdateView(UpdateView):
    model = EmployeePosition
    template_name = "employee/position_update.html"
    form_class = EmployeePositionUpdateForm


employee_position_update_view = EmployeePositionUpdateView.as_view()


class EmployeePositionDeleteView(DeleteView):
    model = EmployeePosition
    template_name = "employee/position_delete.html"


employee_position_delete_view = EmployeePositionDeleteView.as_view()
