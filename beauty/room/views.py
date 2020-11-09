from django.shortcuts import render
from .models import *

def home_page(request):
    service = Service.objects.all()
    feedback = Feedback.objects.all()
    contact = Contacts.objects.all()
    master = Masters.objects.all()
    certificate = Certificate.objects.all()
    context = {'service':service,'feedback':feedback,'contact':contact,'master':master,'certificate':certificate}
    return render(request,'room/home.html',context)


def service_page(request):
    service = Service.objects.all()
    context = {'service':service}
    return render(request,'room/service.html',context)


def feedback_page(request):
    feedback = Feedback.objects.all()
    context = {'feedback':feedback}
    return render(request,'room/feedback.html',context)


def contact_page(request):
    contact = Contacts.objects.all()
    context = {'contact':contact}
    return render(request,'room/contact.html',context)



