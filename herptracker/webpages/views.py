from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .forms import *
import requests


# Create your views here.
def index(request):
    return redirect('home')

def home(request):
    return render(request, 'webpages/home.html')

def entryHerps(request):
    targetURL = reverse('dataEntryHerps')
    actionURL = reverse('herplist')
    form = HerpForm()
    return render(request, 'webpages/entry.html', { 'form': form, 'targetURL': targetURL, 'actionURL': actionURL })

def entryObs(request):
    targetURL = reverse('dataEntryObs')
    actionURL = reverse('obslist')
    form = ObservationForm()
    return render(request, 'webpages/entry.html', { 'form': form, 'targetURL': targetURL, 'actionURL': actionURL })

def analysisHerps(request):
    return render(request, 'webpages/analysis.html')

def analysisObs(request):
    return render(request, 'webpages/analysis.html')

def get_herp_entry(request):
    print(request.data)
    return render(request, 'webpages/entry.html')