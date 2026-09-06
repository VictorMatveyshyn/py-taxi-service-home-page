from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from taxi.models import Driver, Manufacturer, Car


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:

    num_drivers = Driver.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    num_cars = Car.objects.count()
    print(f"{num_drivers=}, {num_manufacturers=}, {num_cars=}")


    return HttpResponse(f"Http request is<br> {request.COOKIES}<br>Hello, world.")