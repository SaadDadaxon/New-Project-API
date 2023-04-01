from django.urls import path
from .views import ContactListCreateView, ContactRUDView


urlpatterns = [
    path('list-create/', ContactListCreateView.as_view()),
    path('rud/<int:pk>', ContactRUDView.as_view()),
]
