from django.urls import path

from api import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('herps/', csrf_exempt(views.HerpList.as_view()), name='herplist'),
    path('herps/<int:herpid>', csrf_exempt(views.HerpDetail.as_view()), name='herpdetail'),
    path('observations/', csrf_exempt(views.ObservationList.as_view()), name='obslist'),
    path('observations/<int:obsid>', csrf_exempt(views.ObservationDetail.as_view()), name='obsdetail'),
]
