from rest_framework import serializers
from ..models import Contact


class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'phone_number', 'email', 'message', 'created_date']
