from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    return redirect('home')

def home(request):
    return render(request, 'webpages/home.html')

def entry(request):
    return render(request, 'webpages/entry.html')

def analysis(request):
    return render(request, 'webpages/analysis.html')