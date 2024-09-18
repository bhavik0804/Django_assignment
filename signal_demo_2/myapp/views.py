
# Create your views here.
# views.py
# views.py
from django.shortcuts import render
from django.contrib.auth.models import User
import threading

def create_user_view(request):
    username = "testuser"
    user, created = User.objects.get_or_create(username=username)
    
    if created:
        print(f"Main view: User '{username}' created in thread {threading.get_ident()}")
    else:
        print(f"Main view: User '{username}' already exists in thread {threading.get_ident()}")
    
    return render(request, 'base.html')

