from auditlog.registry import auditlog
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse

from erp_villa_alemana_escolares_tecnologicos.apps.utils.models import Person


class EmployeeDepartment(models.Model):
    """
    Model representing an employee department.
    """

    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="Department Name",
        help_text="The name of the department.",
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        verbose_name="Department Slug",
        help_text="A short label for URL configuration.",
    )
    description = models.TextField(
        blank=True,
        default="",
        verbose_name="Department Description",
        help_text="A brief description of the department.",
    )

    class Meta:
        verbose_name = "Employee Department"
        verbose_name_plural = "Employee Departments"
        ordering = ["name"]
        constraints = [
            models.UniqueConstraint(
                fields=["name"],
                name="unique_department_name",
            ),
            models.UniqueConstraint(
                fields=["slug"],
                name="unique_department_slug",
            ),
        ]
        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["slug"]),
        ]
        permissions = [
            ("can_view_department", "Can view department"),
            ("can_edit_department", "Can edit department"),
            ("can_delete_department", "Can delete department"),
            ("can_add_department", "Can add department"),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Returns the URL to access a particular department instance.
        """
        return reverse(
            "employees:department-detail",
            kwargs={"department_slug": self.slug},
        )

    def get_employees(self) -> models.QuerySet["Employee"]:
        """
        Returns a queryset of employees in this department.
        """
        return self.employees


class EmployeePosition(models.Model):
    """
    Model representing an employee position.
    """

    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="Position Name",
        help_text="The name of the position.",
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        verbose_name="Position Slug",
        help_text="A short label for URL configuration.",
    )
    description = models.TextField(
        blank=True,
        default="",
        verbose_name="Position Description",
        help_text="A brief description of the position.",
    )

    class Meta:
        verbose_name = "Employee Position"
        verbose_name_plural = "Employee Positions"
        ordering = ["name"]
        constraints = [
            models.UniqueConstraint(
                fields=["name"],
                name="unique_position_name",
            ),
            models.UniqueConstraint(
                fields=["slug"],
                name="unique_position_slug",
            ),
        ]
        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["slug"]),
        ]
        permissions = [
            ("can_view_position", "Can view position"),
            ("can_edit_position", "Can edit position"),
            ("can_delete_position", "Can delete position"),
            ("can_add_position", "Can add position"),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Returns the URL to access a particular position instance.
        """
        return reverse(
            "employees:position-detail",
            kwargs={"position_slug": self.slug},
        )

    def get_employees(self) -> models.QuerySet["Employee"]:
        """
        Returns a queryset of employees in this position.
        """
        return self.employees


class Employee(Person):
    """
    Model representing an employee.
    """

    user = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        related_name="employee",
        verbose_name="User",
        help_text="The user associated with the employee.",
    )
    department = models.ForeignKey(
        EmployeeDepartment,
        on_delete=models.CASCADE,
        related_name="employees",
        verbose_name="Department",
        help_text="The department the employee belongs to.",
    )
    position = models.ForeignKey(
        EmployeePosition,
        on_delete=models.CASCADE,
        related_name="employees",
        verbose_name="Position",
        help_text="The position of the employee.",
    )
    hire_date = models.DateField(
        verbose_name="Hire Date",
        help_text="The date the employee was hired.",
    )

    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Salary",
        help_text="The salary of the employee.",
        validators=[
            MinValueValidator(0),
            MaxValueValidator(9999999.99),
        ],
    )

    class Meta:
        abstract = False
        verbose_name = "Employee"
        verbose_name_plural = "Employees"
        ordering = ["last_name", "first_name"]
        constraints = [
            models.UniqueConstraint(
                fields=["email"],
                name="unique_employee_email",
            ),
        ]
        indexes = [
            models.Index(fields=["last_name"]),
            models.Index(fields=["first_name"]),
        ]
        permissions = [
            ("can_view_employee", "Can view employee"),
            ("can_edit_employee", "Can edit employee"),
            ("can_delete_employee", "Can delete employee"),
            ("can_add_employee", "Can add employee"),
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        """
        Returns the URL to access a particular employee instance.
        """
        return reverse(
            "employees:detail",
            kwargs={"pk": self.pk},
        )


auditlog.register(Employee)
auditlog.register(EmployeeDepartment)
auditlog.register(EmployeePosition)
