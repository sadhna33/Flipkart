from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from customer.serializers import*
# Create your views here.

class GetCustomerViews(APIView):

    def get(self,request):
 
        instance=customer.objects.all()
        serializer=GetcustomerSerializer(instance,many=True)
        return Response(serializer.data)
    
    def post (self,request):
        
        params=request.data 
        print("data",params)
        serializers=GetcustomerSerializer(data=params)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(("message","Save Sucessfully"))
    

class CustomerAddressSerializer(APIView):

    def get(self,request):

        instance=customer.objects.all()
        serializer=CustomerAddressSerializer(instance,many=True)
        return Response(serializer.data)
    
class CustomerDetailAddressView(APIView):
    
    def get(self,request,pk):

        instance = customer.objects.filter(id=pk)
        serializers = CustomerDetailAddressSerializer(instance,many=True)
        return Response(serializer.data)