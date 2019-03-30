from django.shortcuts import render
from django.views.generic import ListView
from .models import Agenda
# Create your views here.

class HomePageView(ListView):
    model = Agenda
    template_name = 'app_agenda/home.html'