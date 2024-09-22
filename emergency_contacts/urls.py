from django.urls import path
from .views import create_contact, list_contacts, delete_contact, redirect_to_contacts

urlpatterns = [
    path("api/contacts/create", create_contact),
    path("api/contacts/", list_contacts),
    path("api/contacts/<int:id>", delete_contact),
    path("", redirect_to_contacts),
]
