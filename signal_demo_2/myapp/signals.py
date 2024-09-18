# myapp/signals.py
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def user_saved_handler(sender, instance, **kwargs):
    print(f"Signal received: Processing start in thread {threading.get_ident()}")
    print("Signal processing done.")
