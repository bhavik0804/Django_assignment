# myapp/apps.py
from django.apps import AppConfig

class MyappConfig(AppConfig):
    name = 'myapp'

    def ready(self):
        import myapp.signals  # This connects the signal when the app is ready
