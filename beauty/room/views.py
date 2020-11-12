from django.shortcuts import render
from .models import *
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
    try:
        customer = Customer.objects.get(id=pk)
        orders = customer.order_set.all()
        orders_count = orders.count()
        filterset = OrderFilterSet(request.GET,queryset=orders)
        orders = filterset.qs # Обращаемся к классу Model
        context = {'customer':customer,'orders':orders,'orders_count':orders_count,'filterset':filterset}
        return render(request,'room/customer.html',context)

    except ObjectDoesNotExist:
        return HttpResponse('Takogo net')


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
    detail = Master.objects.get(id=pk)
    services = detail.service_set.all()
    context = {'detail':detail,'services':services}
    return render(request,'room/details.html',context)


def master_detail(request,pk):
    details = Master.objects.get(id=pk)
    certification = details.certificate_set.all()
    context = {'details':details,'certification':certification}
    return render(request,'room/master_details.html',context)




