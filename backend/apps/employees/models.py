# Imports
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


# Get the user model
User = get_user_model()


# Class based model for the Employee
class Employee(models.Model):
    """
    Model for storing information about employees.
    Attributes:
        emp_id (CharField): A CharField that stores the employee's ID.
        user (OneToOneField): One-to-One relationship with Django's built-in User model.
        address (CharField): A CharField that stores the employee's address.
        department (CharField): A CharField that stores the employee's department.
        position (CharField): A CharField that stores the employee's position.
        salary (DecimalField): A DecimalField that stores the employee's salary.
        hire_date (DateField): A DateField that stores the employee's hire date.
        is_active (BooleanField): A BooleanField that indicates whether the employee is currently active or not.
    """

    emp_id = models.CharField(
        max_length=10,
        primary_key=True,
        verbose_name=_("Employee ID"),
        unique=True,
        editable=False,
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="employee")
    address = models.CharField(
        max_length=255,
        verbose_name=_("Address"),
    )
    department = models.CharField(
        max_length=100,
        verbose_name=_("Department"),
    )
    position = models.CharField(
        max_length=100,
        verbose_name=_("Position"),
    )
    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("Salary"),
    )
    hire_date = models.DateField(
        verbose_name=_("Hire Date"),
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Is Active"),
    )

    # Meta class for the User model
    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def save(self, *args, **kwargs):
        # Generate emp_id if it's not set
        if not self.emp_id:
            # Get the last employee
            last_employee = Employee.objects.order_by().last()

            # If there is a last employee, generate a new emp_id
            if last_employee:
                last_id = int(last_employee.emp_id[3:])  # Extract numeric part
                new_id = f"EMP{str(last_id + 1).zfill(4)}"  # Increment and format

            # If there is no last employee, set emp_id to EMP0001
            else:
                new_id = "EMP0001"  # Initial ID

            # Set the emp_id
            self.emp_id = new_id

        # Call the save method of the parent class
        super().save(*args, **kwargs)

    # String representation of the User model
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
