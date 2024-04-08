# Imports
from django.urls import path
from . import views


# Set the url patters for the home app
urlpatterns = [
    path("", views.RestAPIHome.as_view(), name="restapi_home"),
]
