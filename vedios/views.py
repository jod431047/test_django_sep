from django.shortcuts import render 
from django.views import generic

from .models import Vedio

class VedioList(generic.ListView):
    model = Vedio
