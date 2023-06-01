from rest_framework import serializers
from customer.models import *

class GetcustomerSerializer(serializers.ModelSerializer):

    class Meta:
     model = customer
     fields="__all__"


class CustomeraddressSerializer(serializers.ModelSerializer):
   

   class Meta:
      models = Customer_Address
      fields="__all__"

class CustomerDetailAddressSerializer(serializers.ModelSerializer):
   customer_address = CustomeraddressSerializer(many = True)
   
   class Meta:
      models = customer
      fields= ('first_name','last_name','mobile','age','country','city')
