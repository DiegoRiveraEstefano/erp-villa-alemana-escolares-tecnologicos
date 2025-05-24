from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class ProductCategory(models.Model):
    """
    Model representing a product category.
    """

    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name=_("Product Category Name"),
        help_text=_("The name of the product category."),
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        verbose_name=_("Product Category Slug"),
        help_text=_("A short label for URL configuration."),
    )
    description = models.TextField(
        blank=True,
        default="",
        verbose_name=_("Product Category Description"),
        help_text=_("A brief description of the category."),
    )

    class Meta:
        verbose_name = _("Product Category")
        verbose_name_plural = _("Product Categories")
        ordering = ["name"]
        constraints = [
            models.UniqueConstraint(
                fields=["name"],
                name="unique_product_category_name",
            ),
        ]
        indexes = [
            models.Index(fields=["name"], name="idx_product_category_name"),
            models.Index(fields=["slug"], name="idx_product_category_slug"),
        ]
        permissions = [
            ("can_view_product_category", "Can view product category"),
            ("can_edit_product_category", "Can edit product category"),
            ("can_delete_product_category", "Can delete product category"),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Get URL for product category's detail view.

        Returns:
            str: URL for product category detail.
        """
        return reverse(
            "products:category-detail",
            kwargs={"category_slug": self.slug},
        )


class Product(models.Model):
    """
    Model representing a product.
    """

    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name=_("Product Name"),
        help_text=_("The name of the product."),
    )

    slug = models.SlugField(
        max_length=255,
        unique=True,
        verbose_name=_("Product Slug"),
        help_text=_("A short label for URL configuration."),
    )

    description = models.TextField(
        blank=True,
        default="",
        verbose_name=_("Product Description"),
        help_text="A brief description of the product.",
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("Product Price"),
        help_text=_("The price of the product."),
    )
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.SET_NULL,
        null=True,
        related_name="products",
        verbose_name=_("Product Category"),
        help_text=_("The category to which the product belongs."),
    )

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        ordering = ["name"]
        constraints = [
            models.UniqueConstraint(
                fields=["name"],
                name="unique_product_name",
            ),
            models.UniqueConstraint(
                fields=["slug"],
                name="unique_product_slug",
            ),
        ]
        indexes = [
            models.Index(fields=["name"], name="product_name_idx"),
            models.Index(fields=["slug"], name="product_slug_idx"),
        ]
        permissions = [
            ("can_view_product", "Can view product"),
            ("can_edit_product", "Can edit product"),
            ("can_delete_product", "Can delete product"),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Get URL for product's detail view.

        Returns:
            str: URL for product detail.
        """
        return reverse(
            "products:product-detail",
            kwargs={"product_slug": self.slug},
        )
