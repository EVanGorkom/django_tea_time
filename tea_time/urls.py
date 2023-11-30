# The urls file is like the config/routes file in a rails app


"""
URL configuration for tea_time project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tea_time import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customers/', views.customer_list),
    path('customers/<int:id>', views.customer_detail),
    path('subscriptions/', views.subscription_list),
    path('subscriptions/<int:id>', views.subscription_detail),
    path('teas/', views.tea_list),
    path('teas/<int:id>', views.tea_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)