from django.shortcuts import render, HttpResponse
from .models import Place
# Create your views here.

def places(request):
    places_object = Place.objects.all() #получение таблицы с базы данных
    return render(request, 'places.html',{'placess':places_object})

def primer(request):
    return HttpResponse('primer')