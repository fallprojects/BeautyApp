from django.shortcuts import render
from .models import *

def home_page(request):
    service = Service.objects.all()
    feedback = Feedback.objects.all()
    contact = Contact.objects.all()
    master = Master.objects.all()
    certificate = Certificate.objects.all()
    context = {'service':service,'feedback':feedback,'contact':contact,'master':master,'certificate':certificate}
    return render(request,'room/home.html',context)


def service_page(request):
    services = Service.objects.all()
    context = {'services':services}
    return render(request,'room/service.html',context)


def feedback_page(request):
    feedbacks = Feedback.objects.all()
    context = {'feedbacks':feedbacks}
    return render(request,'room/feedback.html',context)


def contact_page(request):
    contacts = Contact.objects.all()
    context = {'contacts':contacts}
    return render(request,'room/contact.html',context)

def master_page(request):
    masters = Master.objects.all()
    context = {'masters':masters}
    return render(request,'room/master.html',context)


def certificate_page(request):
    certificates = Certificate.objects.all()
    context = {'certificates':certificates}
    return render(request,'room/certificate.html',context)


def service_detail(request,pk):
    detail = Service.objects.get(id=pk)
    context = {'detail':detail}
    return render(request,'room/details.html',context)




