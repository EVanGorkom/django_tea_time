# serializers do exactly the same thing in django as in rails. They format our JSON response.

from rest_framework import serializers
from .models import Customer
from .models import Subscription
from .models import Tea

class CustomerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Customer
    fields = ['id', 'first_name', 'last_name', 'email', 'address']

class SubscriptionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Subscription
    fields = ['id', 'title', 'price', 'frequency', 'customer']

class TeaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tea
    fields = ['id', 'title', 'description', 'temperature', 'brew_time']