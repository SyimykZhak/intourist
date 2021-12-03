from django.urls import path
from .views import profile,HomeView #homepage,

urlpatterns = [
    path('', HomeView.as_view(), name='home_page'),
    path('profile/', profile,name='profile_1')
]

