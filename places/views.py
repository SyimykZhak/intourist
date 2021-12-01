from django.shortcuts import redirect, render, HttpResponse
from .models import Place
from .forms import PlaceForm
# Create your views here.

def places(request):
    places_object = Place.objects.all() #получение таблицы с базы данных
    return render(request, 'places/places.html',{'placess':places_object})

def primer(request):
    return HttpResponse('primer')

def create_place(request):
    if request.method == 'POST':
        place_form = PlaceForm(request.POST)
        if place_form.is_valid():
            place_form.save()
            return redirect(places)

    place_form = PlaceForm()
    return render(request, 'places/form.html', {'place_form': place_form})
 

def place(request, id):
    place_object = Place.objects.get(id=id)
    return render(request, 'places/place.html', {'place_object': place_object })


def edit_place(request, id):
    place_object = Place.objects.get(id=id)

    if request.method == 'POST':
        place_form = PlaceForm(data=request.POST, instance=place_object)
        if place_form.is_valid():
            place_form.save()
            return redirect(place, id=id)

    place_form = PlaceForm(instance=place_object)
    return render(request, 'places/form.html', {'place_form': place_form})


def delete_place(request, id):
    place_object = Place.objects.get(id=id)
    place_object.delete()
    return redirect(places)