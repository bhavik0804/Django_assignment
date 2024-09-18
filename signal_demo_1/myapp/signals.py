# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import time

@receiver(post_save, sender=User)
def user_saved_handler(sender, instance, **kwargs):
    print("Signal received: Processing start.")
    time.sleep(5)  # Simulate heavy processing
    print("Signal processing done.")
