from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic import TemplateView

# These paths are what the client will see, 
# instead of running these views, as in (), we
# instantiate path objects with method references
urlpatterns = [
    path('CheckIn',    views.insert_obs ),
    path('WebCheck',   views.do_web_check),
    path('AllTherms',  views.getTherms, name = 'AllTherms'),
    path('ATherm',     views.getATherm),
    path('AllTemps',   views.getTemps, name= 'AllTemps'),
    path('AddTemp',    views.addTemp, name='AddTemp'),
    path('AddTherm',   views.addTherm, name='AddTherm'),
    path('DeleteThermById/<int:id>',   views.deleteThermById, name='deleteThermById'),
    path('DeleteThermByNameMac/<str:plain_name>/<str:device_mac>',   views.deleteThermByNameMac, name='deleteThermByNameMac'),
    path('', TemplateView.as_view(template_name='home.html') ),

]