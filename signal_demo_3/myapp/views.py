from django.shortcuts import render

# Create your views here.
# myapp/views.py
from django.shortcuts import render
from django.contrib.auth.models import User
import threading

def create_user_view(request):
    try:
        # Start user creation in the view
        print(f"Main view: Starting user creation in thread {threading.get_ident()}")
        user = User.objects.create(username="testuser")

        # Simulate an error after signal execution to trigger rollback
        raise Exception("Forcing rollback after signal")
    except Exception as e:
        print(f"Exception occurred: {e}")
    
    return render(request, 'base.html')
