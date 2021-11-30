from django.urls import path
from .views import homepage,profile

urlpatterns = [
    path('', homepage, name='home_page'),
    path('profile/', profile,name='profile_1')
]

