from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Store(models.Model):
    """
    Model representing a store.
    """

    STORE_TYPE = (
        ("physical", _("Physical Store")),
        ("online", _("Online Store")),
        ("both", _("Both Physical and Online Store")),
    )

    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name=_("Store Name"),
        help_text=_("The name of the store."),
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        verbose_name=_("Store Slug"),
        help_text=_("A short label for URL configuration."),
    )
    description = models.TextField(
        blank=True,
        default="",
        verbose_name=_("Store Description"),
        help_text=_("A brief description of the store."),
    )
    type = models.CharField(
        max_length=16,
        choices=STORE_TYPE,
        default="physical",
        verbose_name=_("Store Type"),
        help_text=_("The type of the store."),
    )
    address = models.ForeignKey(
        "addresses.Address",
        on_delete=models.SET_NULL,
        related_name="stores",
        verbose_name=_("Store Address"),
        help_text=_("The address of the store."),
        null=True,
    )
    warehouse = models.ForeignKey(
        "warehouses.Warehouse",
        on_delete=models.CASCADE,
        related_name="stores",
        verbose_name=_("Warehouse"),
        help_text=_("The warehouse associated with the store."),
    )

    class Meta:
        verbose_name = _("Store")
        verbose_name_plural = _("Stores")
        ordering = ["name"]
        constraints = [
            models.UniqueConstraint(
                fields=["name"],
                name="unique_store_name",
            ),
            models.UniqueConstraint(
                fields=["slug"],
                name="unique_store_slug",
            ),
        ]
        indexes = [
            models.Index(
                fields=["name"],
                name="idx_store_name",
            ),
            models.Index(
                fields=["slug"],
                name="idx_store_slug",
            ),
        ]
        permissions = [
            ("can_view_store", _("Can view store")),
            ("can_edit_store", _("Can edit store")),
            ("can_delete_store", _("Can delete store")),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Returns the URL to access a particular store instance.
        """

        return reverse("stores:store-detail", kwargs={"store_slug": self.slug})


class StoreEmployee(models.Model):
    """
    Model representing an employee in a store.
    """

    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,
        related_name="employees",
        verbose_name=_("Store"),
        help_text=_("The store where the employee works."),
    )
    employee = models.ForeignKey(
        "employees.Employee",
        on_delete=models.CASCADE,
        related_name="store_employees",
        verbose_name=_("Employee"),
        help_text=_("The employee assigned to this store."),
    )
    assigned_date = models.DateField(
        auto_now_add=True,
        verbose_name=_("Assigned Date"),
        help_text=_("The date the employee was assigned to this store."),
    )

    class Meta:
        verbose_name = _("Store Employee")
        verbose_name_plural = _("Store Employees")
        ordering = ["store__name", "employee__last_name", "employee__first_name"]
        constraints = [
            models.UniqueConstraint(
                fields=["store", "employee"],
                name="unique_store_employee_combination",
            ),
        ]
        indexes = [
            models.Index(
                fields=["store"],
                name="idx_store_store",
            ),
            models.Index(
                fields=["employee"],
                name="idx_store_employee",
            ),
        ]
        permissions = [
            ("can_view_store_employee", _("Can view store employee")),
            ("can_edit_store_employee", _("Can edit store employee")),
            ("can_delete_store_employee", _("Can delete store employee")),
        ]

    def __str__(self):
        return (
            f"{self.employee.first_name} {self.employee.last_name} in {self.store.name}"
        )

    def get_absolute_url(self):
        """
        Returns the URL to access a particular store employee instance.
        """
        return reverse("stores:employee-detail", kwargs={"pk": self.pk})
