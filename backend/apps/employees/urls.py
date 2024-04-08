# Imports
from django.urls import path
from . import views


# Set the url patters for the home app
urlpatterns = [
    path(
        "search/<str:emp_id>/",
        views.EmployeeSearchView.as_view(),
        name="employee_search",
    ),
    path(
        "create/",
        views.EmployeeCreateView.as_view(),
        name="employee_create",
    ),
    path(
        "update/<str:emp_id>/",
        views.EmployeeUpdateView.as_view(),
        name="employee_update",
    ),
    path(
        "delete/<str:emp_id>/",
        views.EmployeeDeleteView.as_view(),
        name="employee_delete",
    ),
    path(
        "authenticate/",
        views.EmployeeAuthView.as_view(),
        name="employee_authenticate",
    ),
]
