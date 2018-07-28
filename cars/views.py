from django.shortcuts import render

from django.http import HttpResponse

from .models import Car


def index(request):
    my_car = Car(license_plate = '3SNT836', vin = 'JS9463GDHSGEI1334', year = '1996')
    my_car.save()
    output = Car.objects.all()
    return HttpResponse(output)

def detail(request, car_id):
    return HttpResponse("You\'re looking at %s." % car_id)

def results(request, car_id):
    response = "You're looking at car # %s. Mother Fucker."
    return HttpResponse(response % car_id)

def vote(request, car_id):
    return HttpResponse("You're voting on car %s." % car_id)