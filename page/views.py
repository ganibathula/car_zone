from django.shortcuts import render
from .models import Team
from cars.models import car_model
# Create your views here.
def home(request):
    teams=Team.objects.all()
    featured_cars=car_model.objects.order_by('-created_date').filter(is_featured=True)
    all_cars=car_model.objects.order_by('-created_date')
    data ={
        'teams':teams,
        'featured_cars':featured_cars,
        'all_cars':all_cars,
    }
    return render(request,'templates/page/home.html',data)

def about_page(request):
    teams=Team.objects.all()
    data={
        'teams':teams,
    }
    return render(request,'templates/page/about.html',data)

def service_page(request):
    return render(request,'page/service.html')

def contact_page(request):
    return render(request,'page/contact.html')

