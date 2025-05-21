from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Warehouse(models.Model):
    """
    Model representing a warehouse.
    """

    TYPE = (
        ("main", _("Main Warehouse")),
        ("secondary", _("Secondary Warehouse")),
        ("third_party", _("Third Party Warehouse")),
        ("virtual", _("Virtual Warehouse")),
        ("external", _("External Warehouse")),
    )
    address = models.ForeignKey(
        "addresses.Address",
        on_delete=models.CASCADE,
        related_name="warehouses",
        verbose_name=_("Warehouse Address"),
        help_text=_("The address of the warehouse."),
    )

    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name=_("Warehouse Name"),
        help_text=_("The name of the warehouse."),
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        verbose_name=_("Warehouse Slug"),
        help_text=_("A short label for URL configuration."),
    )
    description = models.TextField(
        blank=True,
        default="",
        verbose_name=_("Warehouse Description"),
        help_text=_("A brief description of the warehouse."),
    )
    type = models.CharField(
        max_length=16,
        choices=TYPE,
        default="main",
        verbose_name=_("Warehouse Type"),
        help_text=_("The type of the warehouse."),
    )

    class Meta:
        verbose_name = _("Warehouse")
        verbose_name_plural = _("Warehouses")
        ordering = ["name"]
        constraints = [
            models.UniqueConstraint(
                fields=["name"],
                name="unique_warehouse_name",
            ),
            models.UniqueConstraint(
                fields=["slug"],
                name="unique_warehouse_slug",
            ),
        ]
        indexes = [
            models.Index(
                fields=["name"],
                name="idx_warehouse_name",
            ),
            models.Index(
                fields=["slug"],
                name="idx_warehouse_slug",
            ),
        ]
        permissions = [
            ("can_view_warehouse", "Can view warehouse"),
            ("can_edit_warehouse", "Can edit warehouse"),
            ("can_delete_warehouse", "Can delete warehouse"),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Returns the URL to access a particular warehouse instance.
        """
        return reverse(
            "warehouses:detail",
            kwargs={"slug": self.slug},
        )


class WarehouseInventory(models.Model):
    """
    Model representing an inventory item.
    """

    product = models.ForeignKey(
        "products.Product",
        on_delete=models.CASCADE,
        related_name="inventories",
        verbose_name=_("Product"),
        help_text=_("The product associated with this inventory item."),
    )
    warehouse = models.ForeignKey(
        Warehouse,
        on_delete=models.CASCADE,
        related_name="inventories",
        verbose_name=_("Warehouse"),
        help_text=_("The warehouse where the product is stored."),
    )
    quantity = models.PositiveIntegerField(
        default=0,
        verbose_name=_("Quantity"),
        help_text=_("The quantity of the product in the warehouse."),
    )

    class Meta:
        verbose_name = _("Warehouse Inventory")
        verbose_name_plural = _("Warehouse Inventories")
        ordering = ["product__name", "warehouse__name"]
        constraints = [
            models.UniqueConstraint(
                fields=["product", "warehouse"],
                name="unique_product_warehouse_combination",
            ),
        ]
        indexes = [
            models.Index(
                fields=["product"],
                name="idx_warehouse_product",
            ),
            models.Index(
                fields=["warehouse"],
                name="idx_warehouse_warehouse",
            ),
        ]
        permissions = [
            ("can_view_warehouse_inventory", "Can view warehouse inventory"),
            ("can_edit_warehouse_inventory", "Can edit warehouse inventory"),
            ("can_delete_warehouse_inventory", "Can delete warehouse inventory"),
        ]

    def __str__(self):
        return f"{self.product.name} in {self.warehouse.name}"

    def get_absolute_url(self):
        """
        Returns the URL to access a particular warehouse inventory instance.
        """
        return reverse(
            "warehouses:inventory-detail",
            kwargs={
                "product_slug": self.product.slug,
                "warehouse_slug": self.warehouse.slug,
            },
        )


class WarehouseEmployee(models.Model):
    """
    Model representing an employee assigned to a warehouse.
    """

    employee = models.ForeignKey(
        "employees.Employee",
        on_delete=models.CASCADE,
        related_name="warehouse_employees",
        verbose_name=_("Employee"),
        help_text=_("The employee assigned to this warehouse."),
    )
    warehouse = models.ForeignKey(
        Warehouse,
        on_delete=models.CASCADE,
        related_name="employees",
        verbose_name=_("Warehouse"),
        help_text=_("The warehouse where the employee works."),
    )

    assigned_date = models.DateField(
        auto_now_add=True,
        verbose_name=_("Assigned Date"),
        help_text=_("The date the employee was assigned to this warehouse."),
    )

    class Meta:
        verbose_name = _("Warehouse Employee")
        verbose_name_plural = _("Warehouse Employees")
        ordering = ["employee__last_name", "employee__first_name"]

        constraints = [
            models.UniqueConstraint(
                fields=["employee", "warehouse"],
                name="unique_employee_warehouse_combination",
            ),
        ]
        indexes = [
            models.Index(
                fields=["employee"],
                name="idx_warehouse_employee",
            ),
            models.Index(
                fields=["warehouse"],
                name="idx_warehouse_warehouse",
            ),
        ]
        permissions = [
            ("can_view_warehouse_employee", "Can view warehouse employee"),
            ("can_edit_warehouse_employee", "Can edit warehouse employee"),
            ("can_delete_warehouse_employee", "Can delete warehouse employee"),
        ]

    def __str__(self):
        return f"{self.employee.first_name} {self.employee.last_name} in {self.warehouse.name}"

    def get_absolute_url(self):
        """
        Returns the URL to access a particular warehouse employee instance.
        """
        return reverse(
            "warehouses:employee-detail",
            kwargs={
                "employee_slug": self.employee.slug,
                "warehouse_slug": self.warehouse.slug,
            },
        )
