from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from erp_villa_alemana_escolares_tecnologicos.apps.warehouses.models import Warehouse

from .models import Sale
from .models import SaleItem


@receiver(pre_save, sender=SaleItem)
def validate_sale_item(sender, instance: SaleItem, **kwargs):
    """
    Validates the Sale instance before saving.
    Ensures that the sale has at least one product and a valid total amount.
    """
    sale: Sale = instance.sale
    warehouse: Warehouse = sale.store.warehouse
    product_inventory = warehouse.get_items().get(
        product__pk=instance.product.pk,
    )
    if instance.quantity > product_inventory.quantity:
        raise ValueError(
            _(
                "The quantity of the product in the sale cannot exceed the available inventory.",
            ),
        )
