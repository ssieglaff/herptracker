from django.urls import path

from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('data/analysis', views.analysis, name='dataAnalysis'),
    path('data/entry', views.entry, name='dataEntry'),
    path('', views.index, name='index')
]
