from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse, HttpRequest
# Create your views here.
from .models import Temp, Thermometer
from .forms import TempForm, ThermForm
from django.contrib import messages

def insert_obs(request) :
    return JsonResponse({"status":'success'},safe=False)


def do_web_check(request):
    x=1
    # t = Temp(therm=123,datetime=989898989,ftemp=35.2)
    return render(request,'hello.html')
    # return HttpResponse('This is an HTTP response')


def getTherms(request: HttpRequest):
    #we don't expect a lot. get the entire queryset
    all_members = Thermometer.objects.all().values('plain_name','device_mac','device_lat','device_lon','device_ele','id')
    if request.GET.get('json','') == 'true':
        data = list(all_members)
        return JsonResponse(data, safe=False)
        
    else:
        return render(request,'showtherms.html',{'all':all_members})

def getATherm(request):
    mac=request.GET.get('mac')
    plain_name = request.GET.get('plain_name')
    qs = Thermometer.objects.filter(device_mac=mac,plain_name=plain_name)
    if qs.count() == 1:
        data = {"mac":qs[0].device_mac,"plain_name":qs[0].plain_name,"id":qs[0].pk}
        return JsonResponse(data,safe=False)
    else:
        return JsonResponse({'noresults':'none'},safe=False)

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

def addTherm(request):
    if request.method == "POST":
        form = ThermForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,('Okay, New Thermometer has been added'))
        else:
            messages.error(request,'Failed Validation')
        if request.POST.get('json')=='true':
            return JsonResponse({'id':form.instance.id})
        else:
            return redirect('AllTherms')
    
    else:
        all_members = Thermometer.objects.all
        return render(request,'addTherm.html',{'all':all_members})


def deleteThermById(request,id):
    therm = Thermometer.objects.get(id=id)
    therm.delete()
    messages.success(request,(f"Item {id} Deleted"))
    return redirect('AllTherms')

def deleteThermByNameMac(request,plain_name,device_mac):
    therm = Thermometer.objects.get(device_mac=device_mac,plain_name=plain_name)
    therm.delete()
    return JsonResponse({'Okay':'none'},safe=False)