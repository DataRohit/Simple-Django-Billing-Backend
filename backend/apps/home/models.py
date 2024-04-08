# Imports
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser


# Class based model for the User
class User(AbstractUser):
    """
    User model that extends Django's AbstractUser model.
    to make them unique and adds first_name and last_name fields.
    Attributes:
        username (CharField): A CharField that stores the username. It is unique and has a maximum length of 30 characters.
        email (EmailField): An EmailField that stores the user's email. It is unique.
        first_name (CharField): A CharField that stores the user's first name. It has a maximum length of 30 characters.
        last_name (CharField): A CharField that stores the user's last name. It has a maximum length of 30 characters.
        phone_number (PhoneNumberField): A CharField that stores the user's phone number. It is validated using a RegexValidator.
    """

    # Declare the fields
    username = models.CharField(
        unique=True,
        verbose_name=_("Username"),
        error_messages={"unique": ("A user with this username already exists!")},
        max_length=30,
    )
    email = models.EmailField(
        unique=True,
        verbose_name=_("Email"),
        error_messages={"unique": ("A user with this email already exists!")},
    )
    first_name = models.CharField(
        max_length=30,
        verbose_name=_("First Name"),
    )
    last_name = models.CharField(
        max_length=30,
        verbose_name=_("Last Name"),
    )
    phone_number = models.CharField(
        max_length=15,
        verbose_name=_("Phone Number"),
        validators=[
            RegexValidator(
                regex=r"^\+\d{1,3}\-\d{9,15}$",
                message=_(
                    "Phone number must be entered in the format: '+[Country Code]-[Phone Number]'. Country code should be 1 to 3 digits and phone number should be between 9 to 15 digits."
                ),
            )
        ],
    )

    # Set the required fields
    REQUIRED_FIELDS = ["email", "first_name", "last_name", "phone_number"]

    # Meta class for the User model
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    # String representation of the User model
    def __str__(self):
        return self.email
