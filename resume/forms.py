from django import forms
from django.db.models import fields
from django.db.models.base import Model
from .models import Contact
from django.forms import ModelForm


class ContactForm(ModelForm):
  class Meta:
    model= Contact
    fields= ['name','email','subject','message']
  
  

