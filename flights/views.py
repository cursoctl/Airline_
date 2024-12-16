from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Flight,Airport,Passenger
from django.urls import reverse 

def index (request):
    return render(request,"flights/index.html",{
        "flights":Flight.objects.all()
    })
def flight(request,flight_id):
    flight=Flight.objects.get(id=flight_id)
    return render(request,"flights/flight.html",{
        "flight":flight,
        "passengers":flight.passengers.all(),
        "non_passengers":passenger.objects.exclude(flights=flight).all()
    })
def book(request,flight_id):
    if request.method == "POST":
        Flight = Flight.objects.get(pk=flight_id)
        passenger=passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight",args=(flight.id)))