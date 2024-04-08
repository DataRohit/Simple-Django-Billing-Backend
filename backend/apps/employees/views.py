# Imports
from django.contrib.auth import get_user_model

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .models import Employee
from .serializers import (
    EmployeeSearchSerializer,
    EmployeeCreateSerializer,
    EmployeeUpdateSerializer,
)


# Get the user model
User = get_user_model()


# Class based view to search the employee
class EmployeeSearchView(APIView):
    # Swagger settings
    @swagger_auto_schema(
        operation_id="employee_search",
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Employee Found",
                schema=EmployeeSearchSerializer,
            ),
            status.HTTP_404_NOT_FOUND: "Employee not found",
        },
        tags=["Employee"],
    )
    def get(self, request, emp_id):
        try:
            employee = EmployeeSearchSerializer(Employee.objects.get(emp_id=emp_id))

            return Response(
                employee.data,
                status=status.HTTP_200_OK,
            )
        except Employee.DoesNotExist:
            return Response(
                {"error": "Employee not found"},
                status=status.HTTP_404_NOT_FOUND,
            )


# Class based view to create an employee
class EmployeeCreateView(APIView):
    # Swagger settings
    @swagger_auto_schema(
        operation_id="employee_create",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "user": openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "username": openapi.Schema(type=openapi.TYPE_STRING),
                        "email": openapi.Schema(type=openapi.TYPE_STRING),
                        "first_name": openapi.Schema(type=openapi.TYPE_STRING),
                        "last_name": openapi.Schema(type=openapi.TYPE_STRING),
                        "phone_number": openapi.Schema(type=openapi.TYPE_STRING),
                    },
                ),
                "password": openapi.Schema(type=openapi.TYPE_STRING),
                "confirm_password": openapi.Schema(type=openapi.TYPE_STRING),
                "address": openapi.Schema(type=openapi.TYPE_STRING),
                "department": openapi.Schema(type=openapi.TYPE_STRING),
                "position": openapi.Schema(type=openapi.TYPE_STRING),
                "salary": openapi.Schema(type=openapi.TYPE_NUMBER),
                "hire_date": openapi.Schema(type=openapi.TYPE_STRING),
                "is_active": openapi.Schema(type=openapi.TYPE_BOOLEAN),
            },
        ),
        responses={
            status.HTTP_201_CREATED: openapi.Response(
                schema=EmployeeCreateSerializer,
                description="Employee Created",
            ),
            status.HTTP_400_BAD_REQUEST: "Invalid Data",
        },
        tags=["Employee"],
    )

    # Post method to create an employee
    def post(self, request):
        # Serialize the data
        serializer = EmployeeCreateSerializer(data=request.data)

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


# Class based view to update an employee
class EmployeeUpdateView(APIView):
    # Swagger settings
    @swagger_auto_schema(
        operation_id="employee_update",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "user": openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "username": openapi.Schema(type=openapi.TYPE_STRING),
                        "email": openapi.Schema(type=openapi.TYPE_STRING),
                        "first_name": openapi.Schema(type=openapi.TYPE_STRING),
                        "last_name": openapi.Schema(type=openapi.TYPE_STRING),
                        "phone_number": openapi.Schema(type=openapi.TYPE_STRING),
                    },
                ),
                "address": openapi.Schema(type=openapi.TYPE_STRING),
                "department": openapi.Schema(type=openapi.TYPE_STRING),
                "position": openapi.Schema(type=openapi.TYPE_STRING),
                "salary": openapi.Schema(type=openapi.TYPE_NUMBER),
                "hire_date": openapi.Schema(type=openapi.TYPE_STRING),
                "is_active": openapi.Schema(type=openapi.TYPE_BOOLEAN),
            },
        ),
        responses={
            status.HTTP_200_OK: openapi.Response(
                schema=EmployeeUpdateSerializer,
                description="Employee Updated",
            ),
            status.HTTP_400_BAD_REQUEST: "Invalid Data",
        },
        tags=["Employee"],
    )

    # Put method to update an employee
    def put(self, request, emp_id):
        try:
            # Get the employee
            employee = Employee.objects.get(emp_id=emp_id)

            # Serialize the data
            serializer = EmployeeUpdateSerializer(employee, data=request.data)

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

        except Employee.DoesNotExist:
            return Response(
                {"error": "Employee not found"},
                status=status.HTTP_404_NOT_FOUND,
            )


# Class based view to delete an employee
class EmployeeDeleteView(APIView):
    # Swagger settings
    @swagger_auto_schema(
        operation_id="employee_delete",
        responses={
            status.HTTP_204_NO_CONTENT: "Employee Deleted",
            status.HTTP_404_NOT_FOUND: "Employee not found",
        },
        tags=["Employee"],
    )

    # Method to delete the employee
    def delete(self, request, emp_id):
        try:
            # Get the employee
            employee = Employee.objects.get(emp_id=emp_id)

            # Get the user and delete it
            user = User.objects.get(username=employee.user.username)

            # Delete the employee
            employee.delete()

            # Delete the user
            user.delete()

            # Return the response
            return Response(
                status=status.HTTP_204_NO_CONTENT,
            )

        except Employee.DoesNotExist:
            return Response(
                {"error": "Employee not found"},
                status=status.HTTP_404_NOT_FOUND,
            )


# Class based view to authenticate an employee and check if active
class EmployeeAuthView(APIView):
    # Set permission to allow any
    permission_classes = [AllowAny]

    # Swagger settings
    @swagger_auto_schema(
        operation_id="employee_auth",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "username": openapi.Schema(type=openapi.TYPE_STRING),
                "password": openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Employee Authenticated",
                schema=EmployeeSearchSerializer,
            ),
            status.HTTP_400_BAD_REQUEST: "Invalid Data",
            status.HTTP_401_UNAUTHORIZED: "Invalid Credentials / Employeee Not Active",
            status.HTTP_404_NOT_FOUND: "Employee not found",
        },
        tags=["Employee"],
    )

    # Method to check if employee exist
    def post(self, request):
        # Get the username and password
        username = request.data.get("username")
        password = request.data.get("password")

        # Check if the username and password is provided
        if not username or not password:
            return Response(
                {"error": "Username and password is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            # Get the user
            user = User.objects.get(username=username)

            # Check if the password is correct
            if user.check_password(password):
                # Get the employee
                employee = EmployeeSearchSerializer(Employee.objects.get(user=user))

                # Check if the employee is active
                if employee.data["is_active"]:
                    return Response(
                        employee.data,
                        status=status.HTTP_200_OK,
                    )
                else:
                    return Response(
                        {"error": "Employee is not active"},
                        status=status.HTTP_401_UNAUTHORIZED,
                    )
            else:
                return Response(
                    {"error": "Invalid Credentials"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )

        except User.DoesNotExist:
            return Response(
                {"error": "Employee not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
