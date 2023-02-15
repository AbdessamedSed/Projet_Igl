from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render
from rest_framework import generics , mixins ,permissions ,authentication
from .serializers import ContactSerializer ,ContactDetailSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Contact
############################################
class ContactDetailAPIView(generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        queryset = Contact.objects.get(pk=int(self.kwargs['id']))
        data = ContactDetailSerializer(queryset).data
        return Response(data)
###########################################

class ContactListAPView(generics.ListCreateAPIView):
    def get(self,serializer):
        queryset = Contact.objects.filter(utilisateur_id=self.request.user.id)
        data =ContactDetailSerializer(queryset,many=True).data
        return Response(data)

##########################################""

class ContactCreateAPView(generics.CreateAPIView):
    queryset=Contact.objects.all()
    serializer_class=ContactSerializer

    def perform_create(self,serializer):
        serializer.save(utilisateur_id=self.request.user)
