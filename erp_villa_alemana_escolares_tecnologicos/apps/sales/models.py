from django.db import models
from django.urls import reverse
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _


class Sale(models.Model):
    """
    Model representing a sale.
    """

    PAYMENT_METHODS = (
        ("CASH", _("Cash")),
        ("CARD", _("Card")),
        ("TRANSFER", _("Transfer")),
    )

    SALE_STATUS = (
        ("PENDING", _("Pending")),
        ("COMPLETED", _("Completed")),
        ("CANCELED", _("Canceled")),
        ("REFUNDED", _("Refunded")),
    )

    customer = models.ForeignKey(
        "customers.Customer",
        on_delete=models.CASCADE,
        related_name="sales",
        verbose_name=_("Customer"),
        help_text=_("The customer making the purchase."),
    )

    store = models.ForeignKey(
        "stores.Store",
        on_delete=models.CASCADE,
        related_name="sales",
        verbose_name=_("Store"),
        help_text=_("The store where the sale was made."),
    )

    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("Price"),
        help_text=_("The price of the product."),
    )

    payment_method = models.CharField(
        max_length=32,
        choices=PAYMENT_METHODS,
        default="CASH",
        verbose_name=_("Payment Method"),
        help_text=_("The payment method used for the sale."),
    )

    status = models.CharField(
        max_length=32,
        choices=SALE_STATUS,
        default="PENDING",
        verbose_name=_("Sale Status"),
        help_text=_("The status of the sale."),
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created At"),
        help_text=_("The date and time when the sale was created."),
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Updated At"),
        help_text=_("The date and time when the sale was last updated."),
    )

    class Meta:
        verbose_name = _("Sale")
        verbose_name_plural = _("Sales")
        ordering = ["-created_at"]
        constraints = [
            models.UniqueConstraint(
                fields=["customer", "created_at"],
                name="unique_sale_customer_created_at",
            ),
        ]
        indexes = [
            models.Index(
                fields=["customer"],
                name="idx_sale_customer",
            ),
            models.Index(
                fields=["created_at"],
                name="idx_sale_created_at",
            ),
        ]
        permissions = [
            ("can_view_sale", "Can view sale"),
            ("can_edit_sale", "Can edit sale"),
            ("can_delete_sale", "Can delete sale"),
        ]

    def __str__(self):
        return f"Sale {self.pk} - {self.customer.first_name} {self.customer.last_name}"

    def get_absolute_url(self):
        """
        Returns the URL to access a particular sale instance.
        """
        return reverse(
            "sales:detail",
            kwargs={"pk": self.pk},
        )


class SaleItem(models.Model):
    """
    Model representing an item in a sale.
    """

    sale = models.ForeignKey(
        Sale,
        on_delete=models.CASCADE,
        related_name="items",
        verbose_name=_("Sale"),
        help_text=_("The sale to which this item belongs."),
    )
    product = models.ForeignKey(
        "products.Product",
        on_delete=models.CASCADE,
        related_name="sale_items",
        verbose_name=_("Product"),
        help_text=_("The product being sold."),
    )
    quantity = models.PositiveIntegerField(
        verbose_name=_("Quantity"),
        help_text=_("The quantity of the product sold."),
    )

    class Meta:
        verbose_name = _("Sale Item")
        verbose_name_plural = _("Sale Items")
        ordering = ["sale", "product"]
        constraints = [
            models.UniqueConstraint(
                fields=["sale", "product"],
                name="unique_sale_item_sale_product",
            ),
        ]
        indexes = [
            models.Index(
                fields=["sale"],
                name="idx_sale_item_sale",
            ),
            models.Index(
                fields=["product"],
                name="idx_sale_item_product",
            ),
        ]
        permissions = [
            ("can_view_sale_item", "Can view sale item"),
            ("can_edit_sale_item", "Can edit sale item"),
            ("can_delete_sale_item", "Can delete sale item"),
        ]

    def __str__(self):
        return f"Sale Item {self.pk} - {self.product.name} (Sale: {self.sale.pk})"

    def get_absolute_url(self):
        """
        Returns the URL to access a particular sale item instance.
        """
        return reverse(
            "sales:saleitem_detail",
            kwargs={"pk": self.pk},
        )

    @cached_property
    def get_total_price(self):
        """
        Returns the total price of the sale item.
        """
        return self.product.price * self.quantity
