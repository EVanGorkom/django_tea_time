from django.contrib import admin
from .models import Customer
from .models import Subscription
from .models import Tea

admin.site.register(Customer)
admin.site.register(Subscription)
admin.site.register(Tea)
