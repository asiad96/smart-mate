from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Contact
from .serializers import ContactSerializer


# Create your views here.
@api_view(["POST"])
def create_contact(request):
    if request.method == "POST":

        serializer = ContactSerializer(
            data=request.data
        )  # pass the data to the serializer

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )  # returns the contact's data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def list_contacts(request):
    contacts = Contact.objects.all()
    serializer = ContactSerializer(
        contacts, many=True
    )  # tells the serializer that you're passing a queryset
    return Response(serializer.data)


@api_view(["DELETE"])
def delete_contact(request, id):
    try:
        contact = Contact.objects.get(id=id)
        contact.delete()
        return Response(
            {"message": "Contact not found"}, status=status.HTTP_404_NOT_FOUND
        )
    except Contact.DoesNotExist:
        return Response(
            {"message": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT
        )


def redirect_to_contacts(request):
    return redirect("/api/contacts/")
