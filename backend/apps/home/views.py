# Imports
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


# Class based view for the home endpoint
class RestAPIHome(generics.GenericAPIView, IsAuthenticated):
    """
    This class-based view handles the home endpoint of the REST API.
    """

    # Swagger settings
    @swagger_auto_schema(
        operation_id="restapi_home",
        operation_description="Welcome to the On Counter Billing System REST API",
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Welcome to the On Counter Billing System REST API",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "message": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Welcome message",
                        ),
                        "status": openapi.Schema(
                            type=openapi.TYPE_INTEGER,
                            description="Status code",
                        ),
                    },
                ),
            )
        },
        tags=["RestAPI Home"],
    )
    def get(self, request):
        """
        This method handles the GET request for the home endpoint.
        It returns a welcome message and a status code.
        """

        # Return the response
        return Response(
            {
                "message": "Welcome to the On Counter Billing System REST API",
                "status": status.HTTP_200_OK,
            }
        )
