# Imports
from django.urls import path
from . import views


# Set the url patterns for the customers app
urlpatterns = [
    path(
        "search/<str:cust_id>/",
        views.CustomerSearchView.as_view(),
        name="search_customer",
    ),
    path("create/", views.CustomerCreateView.as_view(), name="create_customer"),
    path(
        "update/<str:cust_id>/",
        views.CustomerUpdateView.as_view(),
        name="update_customer",
    ),
    path(
        "delete/<str:cust_id>/",
        views.CustomerDeleteView.as_view(),
        name="delete_customer",
    ),
]
