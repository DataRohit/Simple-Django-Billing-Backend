# Imports
from django.urls import path
from . import views


# Set url patterns
urlpatterns = [
    path(
        "create/",
        views.BillCreateView.as_view(),
        name="bill_create",
    ),
    path(
        "search/<str:bill_id>/",
        views.BillSearchView.as_view(),
        name="bill_search",
    ),
]
