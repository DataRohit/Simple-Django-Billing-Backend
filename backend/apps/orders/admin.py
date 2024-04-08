# Imports
from django.contrib import admin
from .models import Order, CheckoutBill


# Register the models
admin.site.register(Order)
admin.site.register(CheckoutBill)
