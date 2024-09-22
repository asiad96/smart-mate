from django.urls import path
from .views import create_contact, list_contacts, delete_contact

urlpatterns = [
    path("api/contacts/create", create_contact),
    path("api/contacts/", list_contacts),
    path("api/contacts/<int:id>", delete_contact),
]
