# Imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .serializers import CheckoutBillSerializer
from .models import CheckoutBill


# Class based view to create a bill
class BillCreateView(APIView):
    # Swagger settings
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "emp_id": openapi.Schema(type=openapi.TYPE_STRING),
                "cust_id": openapi.Schema(type=openapi.TYPE_STRING),
                "orders": openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            "item_id": openapi.Schema(type=openapi.TYPE_STRING),
                            "quantity": openapi.Schema(type=openapi.TYPE_INTEGER),
                            "unit_price": openapi.Schema(
                                type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT
                            ),
                        },
                    ),
                ),
            },
        ),
        responses={201: "Created", 400: "Bad Request"},
        tags=["Bill"],
    )

    # Post method to create a bill
    def post(self, request, format=None):
        # Deserialize the data for the bill
        bill_data = request.data

        # Now create the bill with associated orders
        bill_serializer = CheckoutBillSerializer(data=bill_data)
        if bill_serializer.is_valid():
            bill_serializer.save()
            return Response(bill_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(bill_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Class based view to search for a bill
class BillSearchView(APIView):
    # Swagger settings
    @swagger_auto_schema(
        responses={200: "OK", 404: "Not Found"},
        tags=["Bill"],
    )

    # Get method to search for a bill
    def get(self, request, bill_id, format=None):
        # If the bill ID is not provided, return a 404 response
        if not bill_id:
            return Response(
                {"error": "Bill ID is required"}, status=status.HTTP_404_NOT_FOUND
            )

        # Search for the bill with the given ID
        try:
            bill = CheckoutBill.objects.get(bill_id=bill_id)
            bill_serializer = CheckoutBillSerializer(bill)
            return Response(bill_serializer.data, status=status.HTTP_200_OK)
        except CheckoutBill.DoesNotExist:
            return Response(
                {"error": f"Bill with ID {bill_id} does not exist"},
                status=status.HTTP_404_NOT_FOUND,
            )
