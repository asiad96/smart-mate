from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Contact
from .serializers import ContactSerializer


# Create your views here.
@api_view(["GET", "POST"])
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
    elif request.method == "GET":
        contacts = Contact.objects.all()
        serializer = ContactSerializer(
            contacts, many=True
        )  # tells the serializer that you're passing a queryset
        return Response(serializer.data)
