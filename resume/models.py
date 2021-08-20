from django.db import models
import uuid

from django.shortcuts import redirect
from django.urls import reverse

# Create your models here.

class Contact(models.Model):
  name = models.CharField(max_length=100)
  email=models.EmailField()
  subject=models.CharField(max_length=200)
  message = models.TextField()
  date_created = models.DateTimeField(auto_now_add=True)
  id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
  is_read = models.BooleanField(default=False, null= True)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
      return reverse('message-view',kwargs={'pk':self.pk})
  