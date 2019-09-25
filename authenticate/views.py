from django.shortcuts import render, redirect
from django.views.generic import TemplateView

class Home(TemplateView):
    template_name = 'index.html'

class land(TemplateView):
    template_name = 'landing.html'

def logout(request):
    return redirect('index')

# Create your views here.
