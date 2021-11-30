from django.urls import path
from django.urls.resolvers import URLPattern
from .views import places,primer

urlpatterns = [
    path('', places, name='places_list'),
    path('1', primer, name='places_list'),
]