from django.urls import path
from .views import contact_views

app_name = 'contact'

urlpatterns = [
    path('contact/', contact_views, name='index')
]
