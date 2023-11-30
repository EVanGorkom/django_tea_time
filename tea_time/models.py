# models are models, nothing crazy here, but we can make ALL of our model tables here instead of just one... Need to check and see if that is convention or not though...

from django.db import models

class Tea(models.Model):
  title = models.CharField(max_length=50)
  description = models.CharField(max_length=200)
  temperature = models.IntegerField(default=185)
  brew_time = models.IntegerField(default=4)
  subscriptions = models.ManyToManyField('Subscription')

  def __str__(self):
    return self.title

class Customer(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  email = models.CharField(max_length=50)
  address = models.CharField(max_length=100)

  def __str__(self):
    return self.first_name + ' ' + self.last_name

class Subscription(models.Model):
  title = models.CharField(max_length=50)
  price = models.DecimalField(default=10.00, max_digits=10, decimal_places=2)
  frequency = models.IntegerField(default=1)
  customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

  def __str__(self):
    return self.title