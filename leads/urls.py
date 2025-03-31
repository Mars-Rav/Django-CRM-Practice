from django.urls.conf import path
from .views import *

app_name = "leads"

urlpatterns = [
    path("dashboard", dashboard, name="dashboard"),
    path("create-lead", create_lead, name="create_lead"),
    path("create-form", create_form, name="create_form"),
    path("delete-leads", delete_lead, name="delete_lead"),
    path("<int:slug>", lead_details, name="lead_details"),
    path("<int:id>/edit", edit_lead, name="edit_lead"),
]
