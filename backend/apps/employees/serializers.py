# Imports
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Employee


# Get the user model
User = get_user_model()


# Serializer for the user model
class UserSerializer(serializers.ModelSerializer):
    # Modify the username and email fields
    username = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    phone_number = serializers.CharField(required=False)

    # Meta class for the UserSerializer
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "phone_number"]


class EmployeeSearchSerializer(serializers.ModelSerializer):
    # Set the user field to the UserSerializer
    user = UserSerializer()

    # Meta class for the EmployeeSearchSerializer
    class Meta:
        model = Employee
        fields = [
            "emp_id",
            "user",
            "address",
            "department",
            "position",
            "salary",
            "hire_date",
            "is_active",
        ]


class EmployeeCreateSerializer(serializers.ModelSerializer):
    # Nested serializer for user creation
    user = UserSerializer()
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    # Meta class for the EmployeeCreateSerializer
    class Meta:
        model = Employee
        fields = [
            "user",
            "password",
            "confirm_password",
            "address",
            "department",
            "position",
            "salary",
            "hire_date",
            "is_active",
        ]

    # Method to create the employee
    def create(self, validated_data):
        # Extract user data from validated data
        user_data = validated_data.pop("user")
        password = validated_data.pop("password")
        confirm_password = validated_data.pop("confirm_password")

        if password != confirm_password:
            raise serializers.ValidationError("Passwords do not match")

        # Create user instance
        user = User.objects.create(**user_data, is_superuser=False, is_staff=True)
        # Set the password and save the employee
        user.set_password(password)
        user.save()

        # Create employee instance using the created user
        employee = Employee.objects.create(user=user, **validated_data)

        # Return the employee data
        return employee


class EmployeeUpdateSerializer(serializers.ModelSerializer):
    # Nested serializer for user update
    user = UserSerializer(required=False)
    address = serializers.CharField(required=False)
    department = serializers.CharField(required=False)
    position = serializers.CharField(required=False)
    salary = serializers.FloatField(required=False)
    hire_date = serializers.DateField(required=False)
    is_active = serializers.BooleanField(required=False)

    # Meta class for the EmployeeUpdateSerializer
    class Meta:
        model = Employee
        fields = [
            "user",
            "address",
            "department",
            "position",
            "salary",
            "hire_date",
            "is_active",
        ]

    # Method to update the employee
    def update(self, instance, validated_data):
        # Extract user data from validated data if available
        user_data = validated_data.pop("user", None)

        # Update the user instance if user data is provided
        if user_data:
            user = instance.user
            user.username = user_data.get("username", user.username)
            user.email = user_data.get("email", user.email)
            user.first_name = user_data.get("first_name", user.first_name)
            user.last_name = user_data.get("last_name", user.last_name)
            user.phone_number = user_data.get("phone_number", user.phone_number)
            user.save()

        # Update the employee instance
        instance.address = validated_data.get("address", instance.address)
        instance.department = validated_data.get("department", instance.department)
        instance.position = validated_data.get("position", instance.position)
        instance.salary = validated_data.get("salary", instance.salary)
        instance.hire_date = validated_data.get("hire_date", instance.hire_date)
        instance.is_active = validated_data.get("is_active", instance.is_active)
        instance.save()

        # Return the updated employee data
        return instance
