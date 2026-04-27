from .views import home, result
from django.urls import path

urlpatterns = [
    path('home/', home, name='home'),
    path('/result/', result, name='result'),
]