from django.contrib import admin
from django.urls import path
from . import views

# These paths are what the client will see, 
# instead of running these views, as in (), we
# instantiate path objects with method references
urlpatterns = [
    path('CheckIn',   views.insert_obs ),
    path('WebCheck',  views.do_web_check),
    path('AllTherms', views.getTherms),
    path('AllTemps',  views.getTemps, name= 'AllTemps'),
    path('AddTemps',   views.addTemp, name='NEWPAGE')
]

