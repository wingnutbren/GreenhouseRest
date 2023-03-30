from django import forms
from .models import Temp


class TempForm(forms.ModelForm):
    class Meta:
        model = Temp
        fields = ['therm','datetime','ftemp']