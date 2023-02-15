from rest_framework import serializers
from .models import Contact
class ContactSerializer(serializers.ModelSerializer):
    class Meta :
        model=Contact
        fields =[
           'nom',
           'email',
           'adresse',
           'wilaya',
           'commune',
           'numero_telephone'
        ]
class ContactDetailSerializer(serializers.ModelSerializer):
    class Meta :
        model=Contact
        fields =[
           'nom',
           'email',
           'adresse',
           'wilaya',
           'commune',
           'numero_telephone',
           'pk'
        ]