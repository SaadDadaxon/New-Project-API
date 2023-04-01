from rest_framework.response import Response
from rest_framework import generics, status, permissions
from .serializers import ContactSerializers
from ..models import Contact
from .permission import IsAdminUserOrReadOnly


class ContactListCreateView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializers


class ContactRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializers
    permission_classes = [IsAdminUserOrReadOnly]
