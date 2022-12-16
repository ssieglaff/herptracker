from django.urls import path

from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('data/analysis/herps', views.analysisHerps, name='dataAnalysisHerps'),
    path('data/analysis/observations', views.analysisObs, name='dataAnalysisObs'),
    path('data/entry/herps', views.entryHerps, name='dataEntryHerps'),
    path('data/entry/observations', views.entryObs, name='dataEntryObs'),
    path('', views.index, name='index')
]
