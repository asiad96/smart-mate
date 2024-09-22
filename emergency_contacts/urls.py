from django.urls import path
from . import views

urlpatterns = [
    path("api/contacts/create", views.create_contact),
    path("api/contacts/", views.list_contacts),
    path("api/contacts/<int:id>", views.delete_contact),
    path("", views.api_home),
]
