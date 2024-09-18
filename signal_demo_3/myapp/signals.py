from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db import transaction
import threading

@receiver(post_save, sender=User)
def user_saved_handler(sender, instance, **kwargs):
    print(f"Signal received in thread {threading.get_ident()}")
    # Create another user inside the signal handler
    User.objects.create(username='signal_user')
    print("Signal handler: Created 'signal_user'.")