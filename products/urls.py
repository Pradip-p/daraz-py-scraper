from django.urls import path
from . import views

urlpatterns = [
    #this is url of dashboard
    path('panel/', views.home, name='home')
]