from typing import List
from django.db.models.query_utils import Q
from django.http import response
from django.http.request import QueryDict
from django.test import TestCase
from django.urls import reverse
from django.db.models import QuerySet
from places.models import Place
from  .factory import PlaceFactory

class PlaceslistTestCase(TestCase):
    def test_open_list_success(self):
        place_1 = PlaceFactory(name = 'Cool place', description = 'Visit any time')
        place_2 = PlaceFactory()

        url = reverse('places_list') #/places/
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        places = response.context.get('placess')
        self.assertIsInstance(places, QuerySet)
        print(places)

        self.assertEqual('Location - 1', places[1].location)
        self.assertEqual(places[0].description,'Visit any time')

class PlaceCreateTestCase(TestCase):
        def test_create_place_success(self):
            url = reverse('create-place')
            data ={
                'name': 'Alai', 
                'location': 'Osh', 
                'description': 'region in Kyrgyzstan'
            }
            response = self.client.post(url,data)
            place = Place.objects.last()
            self.assertEqual(place.name, 'Alai')
# Create your tests here.
