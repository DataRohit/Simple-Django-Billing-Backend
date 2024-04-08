# Imports
from django.db import models
from django.utils.translation import gettext_lazy as _


# Class based model for the Order model
class Order(models.Model):
    """
    Model for storing information about the orders
    Attributes:
        order_id (AutoField): An AutoField that stores the order's ID.
        order_date (DateField): A DateField that stores the order's date.
        item_id (CharField): A CharField that stores the item's ID.
        quantity (IntegerField): An IntegerField that stores the quantity of the item.
        unit_price (DecimalField): A DecimalField that stores the unit price of the item.
        total_price (DecimalField): A DecimalField that stores the total price of the order.
    """

    # Fields
    order_id = models.CharField(
        max_length=10,
        primary_key=True,
        verbose_name=_("Order ID"),
        unique=True,
        editable=False,
    )
    order_date = models.DateField(auto_now_add=True, verbose_name=_("Order Date"))
    item_id = models.CharField(max_length=10, verbose_name=_("Item ID"))
    quantity = models.IntegerField(verbose_name=_("Quantity"))
    unit_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_("Unit Price")
    )

    # Calculate field for the total price
    total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    # Calculate the total price
    def save(self, *args, **kwargs):
        # Update the total price
        self.total_price = self.quantity * self.unit_price

        # Generate order_id if it's not set
        if not self.order_id:
            # Get the last order
            last_order = Order.objects.order_by().last()

            # If there is a last order, generate a new order_id
            if last_order:
                last_id = int(last_order.order_id[3:])  # Extract numeric part
                new_id = f"ORD{str(last_id + 1).zfill(4)}"  # Increment and format

            # If there is no last order, set order_id to ORD0001
            else:
                new_id = "ORD0001"  # Initial ID

            # Set the order_id
            self.order_id = new_id

        super(Order, self).save(*args, **kwargs)

    # Metadata
    class Meta:
        ordering = ["order_date"]

    # Methods
    def __str__(self):
        return self.order_id


# Class based model for the CheckoutBill model
class CheckoutBill(models.Model):
    """
    Model for storing information about the bills
    Attributes:
        bill_id (AutoField): An AutoField that stores the bill's ID.
        bill_date (DateField): A DateField that stores the bill's date.
        emp_id (ForeignKey): A ForeignKey that stores the employee's ID.
        cust_id (ForeignKey): A ForeignKey that stores the customer's ID.
        orders (ManyToManyField): A ManyToManyField that stores the order IDs.
        total_price (DecimalField): A DecimalField that stores the total price of the bill.
    """

    # Fields
    bill_id = models.CharField(
        max_length=10,
        primary_key=True,
        verbose_name=_("Bill ID"),
        unique=True,
        editable=False,
    )
    bill_date = models.DateField(auto_now_add=True, verbose_name=_("Bill Date"))
    emp_id = models.ForeignKey(
        "employees.Employee", on_delete=models.CASCADE, verbose_name=_("Employee ID")
    )
    cust_id = models.ForeignKey(
        "customers.Customer", on_delete=models.CASCADE, verbose_name=_("Customer ID")
    )
    orders = models.ManyToManyField(
        "Order", related_name="bills", verbose_name=_("Orders")
    )
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, editable=False, verbose_name=_("Total Price")
    )

    # Calculate the total price
    def save(self, *args, **kwargs):
        # Update the total price
        self.total_price = sum(order.total_price for order in self.orders.all())

        # Generate bill_id if it's not set
        if not self.bill_id:
            # Get the last employee
            last_bill = CheckoutBill.objects.order_by().last()

            # If there is a last bill, generate a new bill_id
            if last_bill:
                last_id = int(last_bill.bill_id[4:])  # Extract numeric part
                new_id = f"BILL{str(last_id + 1).zfill(4)}"  # Increment and format

            # If there is no last bill, set bill_id to BILL0001
            else:
                new_id = "BILL0001"  # Initial ID

            # Set the bill_id
            self.bill_id = new_id

        # Call the save method of the parent class
        super().save(*args, **kwargs)
