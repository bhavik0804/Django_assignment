from django.urls import path
from .views import create_user_view

urlpatterns = [
    path('create_user/', create_user_view, name='create_user'),
]