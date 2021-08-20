from resume.models import Contact
from django.shortcuts import render , redirect
from django.http import HttpResponse
from . forms import ContactForm
from django.contrib import messages
from django.views.generic import CreateView,ListView, DetailView


# Create your views here.

def home(request):
  return render(request,'resume/home.html')

def Contactme(request):
  form = ContactForm()

  if request.method == 'POST':
    form = ContactForm
    if form.is_valid():

      form.save()
      messages.success(request,'Your message has been sent sucesssfully!')
      return redirect('home')

      
  return render(request, 'resume/contactme.html',{'form':form})

def inbox(request):
  messageRequests = Contact.objects.all()
  unreadCount =messageRequests.filter(is_read=False).count()
  context = {'messageRequests':messageRequests,'unreadCount':unreadCount}
  return render(request, 'resume/inbox.html',context)
  
class SendMessageView(CreateView):
  model = Contact
  template_name= 'resume/contactme.html'
  fields= ['name','email','subject','message']

class MessageDetailView(DetailView):
  model = Contact
  template_name = 'resume/view_message.html'
