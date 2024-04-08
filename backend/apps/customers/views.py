# Imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .models import Customer
from .serializers import (
    CustomerSearchSerializer,
    CustomerCreateSerializer,
    CustomerUpdateSerializer,
)


# Class based view to search the customer
class CustomerSearchView(APIView):
    # Swagger settings
    @swagger_auto_schema(
        operation_id="customer_search",
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Customer Found",
                schema=CustomerSearchSerializer,
            ),
            status.HTTP_404_NOT_FOUND: "Customer not found",
        },
        tags=["Customer"],
    )
    def get(self, request, cust_id):
        try:
            customer = CustomerSearchSerializer(Customer.objects.get(cust_id=cust_id))

            return Response(
                customer.data,
                status=status.HTTP_200_OK,
            )
        except Customer.DoesNotExist:
            return Response(
                {"error": "Customer not found"},
                status=status.HTTP_404_NOT_FOUND,
            )


# Class based view to create the customer
class CustomerCreateView(APIView):
    # Swagger settings
    @swagger_auto_schema(
        operation_id="customer_create",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "username": openapi.Schema(type=openapi.TYPE_STRING),
                "email": openapi.Schema(type=openapi.TYPE_STRING),
                "first_name": openapi.Schema(type=openapi.TYPE_STRING),
                "last_name": openapi.Schema(type=openapi.TYPE_STRING),
                "phone_number": openapi.Schema(type=openapi.TYPE_STRING),
                "address": openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        responses={
            status.HTTP_201_CREATED: openapi.Response(
                schema=CustomerCreateSerializer,
                description="Customer Created",
            ),
            status.HTTP_400_BAD_REQUEST: "Invalid Data",
        },
        tags=["Customer"],
    )

    # Post method to create an customer
    def post(self, request):
        # Serialize the data
        serializer = CustomerCreateSerializer(data=request.data)

        # If the data is valid
        if serializer.is_valid():
            # Save the data
            serializer.save()

            # Return the saved data as response
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )

        # Else return the errors
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )


# Class based view to update the customer
class CustomerUpdateView(APIView):
    # Swagger settings
    @swagger_auto_schema(
        operation_id="customer_update",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "username": openapi.Schema(type=openapi.TYPE_STRING),
                "email": openapi.Schema(type=openapi.TYPE_STRING),
                "first_name": openapi.Schema(type=openapi.TYPE_STRING),
                "last_name": openapi.Schema(type=openapi.TYPE_STRING),
                "phone_number": openapi.Schema(type=openapi.TYPE_STRING),
                "address": openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        responses={
            status.HTTP_200_OK: openapi.Response(
                schema=CustomerUpdateSerializer,
                description="Customer Updated",
            ),
            status.HTTP_400_BAD_REQUEST: "Invalid Data",
            status.HTTP_404_NOT_FOUND: "Customer not found",
        },
        tags=["Customer"],
    )

    # Put method to update an customer
    def put(self, request, cust_id):
        try:
            # Get the customer
            customer = Customer.objects.get(cust_id=cust_id)

            # Serialize the data
            serializer = CustomerUpdateSerializer(customer, data=request.data)

            # If the data is valid
            if serializer.is_valid():
                # Save the data
                serializer.save()

                # Return the saved data as response
                return Response(
                    serializer.data,
                    status=status.HTTP_200_OK,
                )

            # Else return the errors
            else:
                return Response(
                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST,
                )

        except Customer.DoesNotExist:
            return Response(
                {"error": "Customer not found"},
                status=status.HTTP_404_NOT_FOUND,
            )


# Class based view to delete the customer
class CustomerDeleteView(APIView):
    # Swagger settings
    @swagger_auto_schema(
        operation_id="customer_delete",
        responses={
            status.HTTP_204_NO_CONTENT: "Customer Deleted",
            status.HTTP_404_NOT_FOUND: "Customer not found",
        },
        tags=["Customer"],
    )

    # Delete method to delete an customer
    def delete(self, request, cust_id):
        try:
            # Get the customer
            customer = Customer.objects.get(cust_id=cust_id)

            # Delete the customer
            customer.delete()

            # Return the response
            return Response(status=status.HTTP_204_NO_CONTENT)

        except Customer.DoesNotExist:
            return Response(
                {"error": "Customer not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
