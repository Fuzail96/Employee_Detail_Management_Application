

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Paypal', include('paypal.standard.ipn.urls')),
    path('', include('myapp.urls')),

]
