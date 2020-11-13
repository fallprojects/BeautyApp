from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from .forms import FeedbackForm
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib import messages
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist


def home_page(request):
    service = Service.objects.all()
    feedback = Feedback.objects.all()
    contact = Contact.objects.all()
    master = Master.objects.all()
    certificate = Certificate.objects.all()
    context = {'service':service,'feedback':feedback,'contact':contact,'master':master,'certificate':certificate}
    return render(request,'room/home.html',context)


def customer_page(request, pk):
    customer = Customer.objects.get(id=pk)
    context = {'customer':customer}
    return render(request,'room/customer.html',context)


def service_page(request):
    services = Service.objects.all()
    context = {'services':services}
    return render(request,'room/service.html',context)


def feedback_page(request):
    feedbacks = Feedback.objects.all()
    form = FeedbackForm()
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'feedbacks':feedbacks,'form':form}
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
    detail = Master.objects.get(id=pk)
    services = detail.service_set.all()
    context = {'detail':detail,'services':services}
    return render(request,'room/details.html',context)


def master_detail(request,pk):
    details = Master.objects.get(id=pk)
    certification = details.certificate_set.all()
    context = {'details':details,'certification':certification}
    return render(request,'room/master_details.html',context)



def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('home')
    context = {'form':form}
    return render(request,'room/register.html',context)

