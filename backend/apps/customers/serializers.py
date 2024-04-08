# Imports
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Customer


# Get the user model
User = get_user_model()


class CustomerSearchSerializer(serializers.ModelSerializer):
    # Meta class for the CustomerSearchSerializer
    class Meta:
        model = Customer
        fields = [
            "cust_id",
            "username",
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "address",
            "is_active",
        ]


class CustomerCreateSerializer(serializers.ModelSerializer):
    # Meta class for the CustomerCreateSerializer
    class Meta:
        model = Customer
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "address",
        ]


class CustomerUpdateSerializer(serializers.ModelSerializer):
    # Set the filelds to not required
    username = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    phone_number = serializers.CharField(required=False)
    address = serializers.CharField(required=False)
    is_active = serializers.BooleanField(required=False)

    # Meta class for the CustomerUpdateSerializer
    class Meta:
        model = Customer
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "address",
            "is_active",
        ]

    def update(self, instance, validated_data):
        instance.username = validated_data.get("username", instance.username)
        instance.email = validated_data.get("email", instance.email)
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.phone_number = validated_data.get(
            "phone_number", instance.phone_number
        )
        instance.address = validated_data.get("address", instance.address)
        instance.is_active = validated_data.get("is_active", instance.is_active)
        instance.save()
        return instance
