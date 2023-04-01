from django.urls import path
from .views import index, detail_art


app_name = 'article'

urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:pk>/', detail_art, name='detail'),
]
