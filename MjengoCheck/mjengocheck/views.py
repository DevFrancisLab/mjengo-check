from django.shortcuts import render

# Create your views here.
# Web Pages
from django.http import HttpResponse

def home(request):
    return render(request,'mjengocheck/home.html',{'title':'Home'})

def about(request):
    return render(request,'mjengocheck/about.html',{'title':'About'})

# Africa's Talking USSD
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Worker, CheckInLog, IncidentReport

@csrf_exempt
def ussd_callback(request):
    session_id = request.POST.get("sessionId", "")
    phone_number = request.POST.get("phoneNumber", "")
    text = request.POST.get("text", "")

    menu = text.split("*")

    if text == "":
        return HttpResponse("CON Welcome to MjengoCheck\n1. Check In\n2. Check Out\n3. Report Incident")
    
    elif menu[0] == "1":
        try:
            worker = Worker.objects.get(phone_number=phone_number)
            CheckInLog.objects.create(worker=worker, status="in")
            return HttpResponse("END You have checked in.")
        except Worker.DoesNotExist:
            return HttpResponse("END You are not registered.")

    elif menu[0] == "2":
        try:
            worker = Worker.objects.get(phone_number=phone_number)
            CheckInLog.objects.create(worker=worker, status="out")
            return HttpResponse("END You have checked out.")
        except Worker.DoesNotExist:
            return HttpResponse("END You are not registered.")

    elif menu[0] == "3":
        if len(menu) == 1:
            return HttpResponse("CON Enter your incident:")
        else:
            try:
                worker = Worker.objects.get(phone_number=phone_number)
                IncidentReport.objects.create(worker=worker, site=worker.site, message=menu[1])
                return HttpResponse("END Incident recorded. Stay safe.")
            except Worker.DoesNotExist:
                return HttpResponse("END You are not registered.")
    
    return HttpResponse("END Invalid input.")
