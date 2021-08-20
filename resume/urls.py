from django.contrib import admin
from django.urls import  path , include
from .views import (
  SendMessageView, 
  MessageDetailView,
)

from . import views

urlpatterns = [
  path('',views.home,name='home'),
  path('contact/',SendMessageView.as_view(),name='contact'),
  path('inbox/',views.inbox,name='inbox'),
  path('messageview/<str:pk>/',MessageDetailView.as_view(),name='message-view'),
]