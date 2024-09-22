from django.urls import path
from .views import create_contact

urlpatterns = [
    path("api/contacts/", create_contact),
]
