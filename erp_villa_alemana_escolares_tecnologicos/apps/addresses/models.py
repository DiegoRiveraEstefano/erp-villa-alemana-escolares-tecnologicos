from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Region(models.Model):
    """Region model.

    Description: This model represents a region.

    Attributes:
        name (CharField): The name of the region.
        cod (CharField): The code of the region.
        number (CharField): The number of the region.

    Example:
        >>> region = Region.objects.create(name="Region 1", cod="R1", number="1")
        >>> region.get_absolute_url()

    Methods:
        __str__ (str): Returns the string representation of the region.
        get_absolute_url (str): Returns the URL for the region.


    """

    name = models.CharField(
        verbose_name=_("Region name"),
        max_length=64,
        unique=True,
        help_text=_("The name of the region."),
    )
    cod = models.CharField(
        verbose_name=_("Region code"),
        max_length=32,
        unique=True,
        help_text=_("The code of the region."),
    )
    number = models.CharField(
        verbose_name=_("Region number"),
        max_length=32,
        unique=True,
        help_text=_("The number of the region."),
    )

    class Meta:
        ordering = ("number",)
        verbose_name = _("Region")
        verbose_name_plural = _("Regions")
        constraints = [
            models.UniqueConstraint(
                fields=["name"],
                name="unique_region_name",
            ),
            models.UniqueConstraint(
                fields=["cod"],
                name="unique_region_cod",
            ),
        ]
        indexes = [
            models.Index(
                fields=["name"],
                name="region_name_idx",
            ),
            models.Index(
                fields=["cod"],
                name="region_cod_idx",
            ),
        ]
        permissions = [
            ("can_add_region", "Can add region"),
            ("can_view_region", "Can view region"),
            ("can_edit_region", "Can edit region"),
            ("can_delete_region", "Can delete region"),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("addresses:region-detail", kwargs={"pk": self.pk})


class Province(models.Model):
    """Province model.

    Description: This model represents a province.

    Attributes:
        region (ForeignKey): The region of the province.
        name (CharField): The name of the province.
        cod (CharField): The code of the province.

    Methods:
        __str__ (str): Returns the string representation of the province.
        get_absolute_url (str): Returns the URL for the province.

    Example:
        >>> province = Province.objects.create(
            region=region, name="Province 1", cod="P1")
        >>> province.get_absolute_url()
        '/addressess/1/provinces/1/'

    """

    region = models.ForeignKey(
        Region,
        verbose_name=_("Province region"),
        on_delete=models.CASCADE,
        related_name="cities",
        help_text=_("The region of the province."),
    )
    name = models.CharField(
        _("Province name"),
        max_length=64,
        unique=True,
        help_text=_("The name of the province."),
    )
    cod = models.CharField(
        _("Province code"),
        max_length=32,
        unique=True,
        help_text=_("The code of the province."),
    )

    class Meta:
        ordering = ("name",)
        verbose_name = _("City")
        verbose_name_plural = _("Cities")
        constraints = [
            models.UniqueConstraint(
                fields=["name"],
                name="unique_province_name",
            ),
            models.UniqueConstraint(
                fields=["cod"],
                name="unique_province_cod",
            ),
        ]
        indexes = [
            models.Index(
                fields=["name"],
                name="province_name_idx",
            ),
            models.Index(
                fields=["cod"],
                name="province_cod_idx",
            ),
        ]
        permissions = [
            ("can_view_province", "Can view province"),
            ("can_edit_province", "Can edit province"),
            ("can_delete_province", "Can delete province"),
            ("can_add_province", "Can add province"),
        ]

    def __str__(self):
        return f"{self.region} - {self.name}"

    def get_absolute_url(self):
        return reverse("addresses:city-detail", kwargs={"pk": self.pk})


class Comuna(models.Model):
    """Comuna model.

    Description: This model represents a comuna.

    Attributes:
        province (ForeignKey): The province of the comuna.
        name (CharField): The name of the comuna.
        cod (CharField): The code of the comuna.

    Methods:
        __str__ (str): Returns the string representation of the comuna.
        get_absolute_url (str): Returns the URL for the comuna.

    Example:
        >>> comuna = Comuna.objects.create(province=province, name="Comuna 1", cod="C1")
        >>> comuna.get_absolute_url()
        '/addressess/1/comunas/1/'

    """

    province = models.ForeignKey(
        Province,
        verbose_name=_("Comuna province"),
        on_delete=models.CASCADE,
        related_name="comunas",
        help_text=_("The province of the comuna."),
    )
    name = models.CharField(
        _("Comuna name"),
        max_length=64,
        unique=True,
        help_text=_("The name of the comuna."),
    )
    cod = models.CharField(
        _("Comuna code"),
        max_length=32,
        unique=True,
        help_text=_("The code of the comuna."),
    )

    class Meta:
        ordering = ("name",)
        verbose_name = _("Comuna")
        verbose_name_plural = _("Comunas")
        constraints = [
            models.UniqueConstraint(
                fields=["name"],
                name="unique_comuna_name",
            ),
            models.UniqueConstraint(
                fields=["cod"],
                name="unique_comuna_cod",
            ),
        ]
        indexes = [
            models.Index(
                fields=["name"],
                name="comuna_name_idx",
            ),
            models.Index(
                fields=["cod"],
                name="comuna_cod_idx",
            ),
        ]
        permissions = [
            ("can_view_comuna", "Can view comuna"),
            ("can_edit_comuna", "Can edit comuna"),
            ("can_delete_comuna", "Can delete comuna"),
            ("can_add_comuna", "Can add comuna"),
        ]

    def __str__(self):
        return f"{self.province} - {self.name}"

    def get_absolute_url(self):
        return reverse("addresses:comuna-detail", kwargs={"pk": self.pk})


class Address(models.Model):
    comuna = models.ForeignKey(
        Comuna,
        verbose_name=_("Comuna"),
        on_delete=models.CASCADE,
        related_name="addresses",
        help_text=_("The comuna of the address."),
    )

    street = models.CharField(
        _("Street name"),
        max_length=96,
        help_text=_("Street name"),
    )
    number = models.PositiveSmallIntegerField(
        _("Street Number"),
        help_text=_("Street number"),
    )
    apartment = models.CharField(
        _("Apartment"),
        max_length=16,
        blank=True,
        default="",
        help_text=_("Apartment number"),
    )
    floor = models.CharField(
        _("Floor"),
        max_length=16,
        blank=True,
        default="",
        help_text=_("Floor number"),
    )
    description = models.TextField(
        _("Description"),
        blank=True,
        default="",
        help_text=_("A brief description of the address."),
    )
    postal_code = models.CharField(
        _("Postal Code"),
        max_length=20,
        blank=True,
        default="",
        help_text=_("The postal code of the address."),
    )

    class Meta:
        verbose_name = _("Address")
        verbose_name_plural = _("Addresses")
        ordering = ("street", "number")
        constraints = [
            models.UniqueConstraint(
                fields=["street", "number"],
                name="unique_address_street_number",
            ),
        ]
        indexes = [
            models.Index(
                fields=["street"],
                name="address_street_idx",
            ),
            models.Index(
                fields=["number"],
                name="address_number_idx",
            ),
        ]
        permissions = [
            ("can_view_address", "Can view address"),
            ("can_edit_address", "Can edit address"),
            ("can_delete_address", "Can delete address"),
            ("can_add_address", "Can add address"),
        ]

    def __str__(self):
        return f"{self.comuna} - {self.street}.{self.number}"

    def get_absolute_url(self):
        return reverse("addresses:detail", kwargs={"pk": self.pk})
