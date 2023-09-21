from django.urls import path
from .views import shortner

urlpatterns = [
    path('',shortner,name='shortner'),
    
]

