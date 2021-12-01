from django.urls import path
from django.urls.resolvers import URLPattern
from .views import places,primer,create_place,place, \
    edit_place,delete_place

urlpatterns = [
    path('', places, name='places_list'),
    path('primer', primer, name='places_1'),
    path('create/', create_place, name='create-place'),
    path('<int:id>/', place,name='place'),
    path('<int:id>/edit/', edit_place,name='edit-place'),
    path('<int:id>/delete/', delete_place,name='delete-place'),
]