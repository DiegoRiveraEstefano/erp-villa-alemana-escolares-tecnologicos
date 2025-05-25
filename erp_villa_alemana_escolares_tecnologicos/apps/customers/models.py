from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from erp_villa_alemana_escolares_tecnologicos.apps.utils.models import Person


class Customer(Person):
    """
    Model representing a customer.
    """

    address = models.ForeignKey(
        "addresses.Address",
        on_delete=models.SET_NULL,
        related_name="customers",
        verbose_name=_("Customer Address"),
        help_text=_("The address of the customer."),
        null=True,
    )

    class Meta:
        verbose_name = _("Customer")
        verbose_name_plural = _("Customers")
        ordering = ["first_name", "last_name"]
        constraints = [
            models.UniqueConstraint(
                fields=["email"],
                name="unique_customer_email",
            ),
            models.UniqueConstraint(
                fields=["phone_number"],
                name="unique_customer_phone_number",
            ),
        ]
        indexes = [
            models.Index(
                fields=["first_name"],
                name="idx_customer_first_name",
            ),
            models.Index(
                fields=["last_name"],
                name="idx_customer_last_name",
            ),
        ]
        permissions = [
            ("can_view_customer", "Can view customer"),
            ("can_edit_customer", "Can edit customer"),
            ("can_delete_customer", "Can delete customer"),
            ("can_add_customer", "Can add customer"),
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        """
        Returns the URL to access a particular customer instance.
        """
        return reverse(
            "customers:customer-detail",
            kwargs={"pk": self.pk},
        )
