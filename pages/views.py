from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"

class TestPageView(TemplateView):
    """just a view to test qr with pet"""
    template_name =  "pet.html"

