# The views of a django app act like the controllers of a rails app. We create the CRUD methods/functions here

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Customer, Subscription, Tea
from .serializers import CustomerSerializer, SubscriptionSerializer, TeaSerializer


# Customer CRUD Functions
@api_view(['GET', 'POST'])
def customer_list(request, format=None):
  if request.method == 'GET':
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many = True)
    return Response(serializer.data)
  
  elif request.method == 'POST':
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(['GET', 'PUT', 'DELETE'])
def customer_detail(request, id, format=None):
  try:
    customer = Customer.objects.get(pk=id)
  except Customer.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  if request.method == 'GET':
    serializer = CustomerSerializer(customer)
    return Response(serializer.data)
  
  elif request.method == 'PUT':
    serializer = CustomerSerializer(customer, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  elif request.method == 'DELETE':
    customer.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  

# Subscription CRUD Functions
@api_view(['GET', 'POST'])
def subscription_list(request, format=None):
  if request.method == 'GET':
    subscriptions = Subscription.objects.all()
    serializer = SubscriptionSerializer(subscriptions, many = True)
    return Response(serializer.data)
  
  elif request.method == 'POST':
    serializer = SubscriptionSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(['GET', 'PUT', 'DELETE'])
def subscription_detail(request, id, format=None):
  try:
    subscription = Subscription.objects.get(pk=id)
  except subscription.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  if request.method == 'GET':
    serializer = SubscriptionSerializer(subscription)
    return Response(serializer.data)
  
  elif request.method == 'PUT':
    serializer = SubscriptionSerializer(subscription, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  elif request.method == 'DELETE':
    subscription.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  

# Tea CRUD Functions
@api_view(['GET', 'POST'])
def tea_list(request, format=None):
  if request.method == 'GET':
    teas = Tea.objects.all()
    serializer = TeaSerializer(teas, many = True)
    return Response(serializer.data)
  
  elif request.method == 'POST':
    serializer = TeaSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(['GET', 'PUT', 'DELETE'])
def tea_detail(request, id, format=None):
  try:
    tea = Tea.objects.get(pk=id)
  except tea.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  if request.method == 'GET':
    serializer = TeaSerializer(tea)
    return Response(serializer.data)
  
  elif request.method == 'PUT':
    serializer = TeaSerializer(tea, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  elif request.method == 'DELETE':
    tea.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)