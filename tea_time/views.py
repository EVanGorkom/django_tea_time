# The views of a django app act like the controllers of a rails app. We create the CRUD methods/functions here

from django.http import HttpResponse

def index(request):
  return HttpResponse()