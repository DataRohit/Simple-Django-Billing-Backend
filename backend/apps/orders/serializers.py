# Imports
from rest_framework import serializers
from .models import CheckoutBill, Order


# Class based serializer to serialize the order data
class OrderSerializer(serializers.ModelSerializer):
    # Fields
    order_id = serializers.CharField(read_only=True, required=False)
    order_date = serializers.DateField(read_only=True, required=False)
    total_price = serializers.DecimalField(
        read_only=True, required=False, max_digits=10, decimal_places=2
    )

    # Meta class
    class Meta:
        model = Order
        fields = [
            "order_id",
            "order_date",
            "item_id",
            "quantity",
            "unit_price",
            "total_price",
        ]

        # Set read only fields
        read_only_fields = ["order_id", "order_date", "total_price"]


# Class based serializer to serialize the bill data
class CheckoutBillSerializer(serializers.ModelSerializer):
    # Fields
    orders = OrderSerializer(many=True)

    # Meta class
    class Meta:
        model = CheckoutBill
        fields = ["bill_id", "bill_date", "emp_id", "cust_id", "orders", "total_price"]
        read_only_fields = ["bill_id", "bill_date", "total_price"]

    def create(self, validated_data):
        # Get the orders data
        orders_data = validated_data.pop("orders")

        # Create the bill
        bill = CheckoutBill.objects.create(**validated_data)

        # Create the orders and associate them with the bill
        created_orders = []
        for order_data in orders_data:
            order = Order.objects.create(**order_data)
            created_orders.append(order)

        # Add the created orders to the bill
        bill.orders.add(*created_orders)

        # Update the total price of the bill
        total_price = sum([order.total_price for order in created_orders])

        # Set the total price of the bill
        bill.total_price = total_price

        # Save the bill
        bill.save()

        # Return the bill
        return bill
