from django.shortcuts import render

# Create your views here.
def car_view(request):
    return render(request,'cars/car.html')