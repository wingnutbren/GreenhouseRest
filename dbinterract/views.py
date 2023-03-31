from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
# Create your views here.
from .models import Temp, Thermometer
from .forms import TempForm
from django.contrib import messages

def insert_obs(request) :
    return JsonResponse({"status":'success'},safe=False)


def do_web_check(request):
    x=1
    # t = Temp(therm=123,datetime=989898989,ftemp=35.2)
    return render(request,'hello.html')
    # return HttpResponse('This is an HTTP response')


def getTherms(request):
    all_members = Thermometer.objects.all
    return render(request,'showtherms.html',{'all':all_members})

def getATherm(request):
    mac=request.GET.get("mac")
    # r = Thermometer.objects.filter(device_mac=mac)
    oneTherm = Thermometer.objects.get(device_mac=mac)
    data = {"mac":oneTherm.device_mac,"id":oneTherm.pk}
    return JsonResponse(data,safe=False)
    


def getTemps(request):
    all_members = Temp.objects.all
    return render(request,'showtemps.html',{'all':all_members})


def addTemp(request):
    if request.method == "POST":
        form = TempForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,('Okay, everything has been added'))
        else:
            messages.error(request,'Failed Validation')
        return redirect('AllTemps')
    
    else:
        all_members = Thermometer.objects.all
        return render(request,'addtemp.html',{'all':all_members})

