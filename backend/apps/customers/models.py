# Imports
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


# Get the user model
User = get_user_model()


# Class based model for the Customer
class Customer(models.Model):
    """
    Model for storing information about customers.
    Attributes:
        cust_id (CharField): A CharField that stores the customer's ID.
        username (CharField): A CharField that stores the customer's username.
        email (EmailField): An EmailField that stores the customer's email.
        first_name (CharField): A CharField that stores the customer's first name.
        last_name (CharField): A CharField that stores the customer's last name.
        phone_number (CharField): A CharField that stores the customer's phone number.
        address (CharField): A CharField that stores the customer's address.
        is_active (BooleanField): A BooleanField that indicates whether the customer is currently active or not.
    """

    cust_id = models.CharField(
        max_length=10,
        primary_key=True,
        verbose_name=_("Customer ID"),
        unique=True,
        editable=False,
    )
    username = models.CharField(
        max_length=150,
        verbose_name=_("Username"),
        unique=True,
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
    address = models.CharField(
        max_length=255,
        verbose_name=_("Address"),
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Is Active"),
    )

    # Meta class for the User model
    class Meta:
        verbose_name = _("Customer")
        verbose_name_plural = _("Customers")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        # Generate cust_id if it's not set
        if not self.cust_id:
            # Get the last employee
            last_employee = Customer.objects.order_by().last()

            # If there is a last employee, generate a new cust_id
            if last_employee:
                last_id = int(last_employee.cust_id[4:])  # Extract numeric part
                new_id = f"CUST{str(last_id + 1).zfill(4)}"  # Increment and format

            # If there is no last employee, set cust_id to CUST0001
            else:
                new_id = "CUST0001"  # Initial ID

            # Set the cust_id
            self.cust_id = new_id

        # Call the save method of the parent class
        super().save(*args, **kwargs)
