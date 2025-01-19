from django.db import models
from django.utils import timezone

class Contact(models.Model):
    first_name =models.CharField(max_length=50)
    last_name =models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254, blank=True)
    create_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
