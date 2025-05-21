from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group as BaseGroup
from django.db import models
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Default custom user model for ERP Villa alemana Escolares Tecnologicos.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore[assignment]
    last_name = None  # type: ignore[assignment]

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})


class UserGroup(BaseGroup):
    """
    Model representing a group of users.
    """

    slug = CharField(
        verbose_name=_("Group slug"),
        max_length=255,
        unique=True,
        help_text=_("The slug of the group."),
    )

    description = CharField(
        verbose_name=_("Group description"),
        max_length=255,
        blank=True,
        help_text=_("The description of the group."),
    )

    class Meta:
        ordering = ("name",)
        verbose_name = _("Group")
        verbose_name_plural = _("Groups")
        constraints = [
            models.UniqueConstraint(
                fields=["name"],
                name="unique_group_name",
            ),
            models.UniqueConstraint(
                fields=["slug"],
                name="unique_group_slug",
            ),
        ]

    def __str__(self) -> str:
        """String representation of the UserGroup model.

        Returns:
            str: Name of the group.

        """
        return self.name

    def get_absolute_url(self) -> str:
        """Get URL for group's detail view.

        Returns:
            str: URL for group detail.

        """
        return reverse("users:group-detail", kwargs={"slug": self.slug})
