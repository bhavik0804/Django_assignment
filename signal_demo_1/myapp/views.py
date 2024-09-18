from django.shortcuts import render

# Create your views here.

# views.py
# views.py
# views.py
from django.shortcuts import render
from django.contrib.auth.models import User

def create_user_view(request):
    username = "testuser"
    user, created = User.objects.get_or_create(username=username)
    if created:
        print(f"User '{username}' created!")
    else:
        print(f"User '{username}' already exists.")
    
    return render(request, 'base.html')


