# models are models, nothing crazy here, but we can make ALL of our model tables here instead of just one... Need to check and see if that is convention or not though...

from django.db import models

class Tea(models.Model):
  title = models.CharField(max_length=50)
  description = models.CharField(max_length=200)
  temperature = models.FloatField
  brew_time = models.IntegerField
  subscriptions = models.ManyToManyField('Subscription')

class Customer(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  email = models.CharField(max_length=50)
  address = models.CharField(max_length=100)

class Subscription(models.Model):
  title = models.CharField(max_length=50)
  price = models.IntegerField
  frequency = models.IntegerField
  customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

