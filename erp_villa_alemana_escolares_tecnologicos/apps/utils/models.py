from django.db import models


class Person(models.Model):
    """
    Model representing a person.
    """

    rut = models.CharField(
        max_length=13,
        unique=True,
        verbose_name="RUT",
        help_text="The person's RUT (Rol Único Tributario).",
    )
    first_name = models.CharField(
        max_length=255,
        verbose_name="First Name",
        help_text="The person's first name.",
    )
    last_name = models.CharField(
        max_length=255,
        verbose_name="Last Name",
        help_text="The person's last name.",
    )
    email = models.EmailField(
        unique=True,
        verbose_name="Email Address",
        help_text="The person's email address.",
    )
    phone_number = models.CharField(
        max_length=20,
        blank=True,
        default="",
        verbose_name="Phone Number",
        help_text="The person's phone number.",
    )

    class Meta:
        abstract = True
