from django import forms
from .models import Temp, Thermometer


class TempForm(forms.ModelForm):
    class Meta:
        model = Temp
        fields = ['therm','datetime','ftemp']

class ThermForm(forms.ModelForm):
    class Meta:
        model = Thermometer
        fields = ['plain_name' ,'device_mac','device_lat','device_lon','device_ele']