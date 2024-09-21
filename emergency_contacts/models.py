from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

#  to validates format, pretty print and convert phone numbers


# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    # phone_number not optional
    phone_number = PhoneNumberField(blank=False)
