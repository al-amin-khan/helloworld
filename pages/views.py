from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView

# Create your views here.
class HomeTemplateView(TemplateView):
    template_name = 'pages/index.html'


class AboutTemplateView(TemplateView):
    template_name = 'pages/about.html'
