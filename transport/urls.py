from django.urls import path
from transport.views import (CarCreate, CarList, MotorcycleCreate, MotorcycleList, TruckCreate, TruckList)


urlpatterns = [
    path('car/create/', CarCreate.as_view()),
    path('car/', CarList.as_view()),
    path('motorcycle/create/', MotorcycleCreate.as_view()),
    path('motorcycle/', MotorcycleList.as_view()),
    path('truck/create/', TruckCreate.as_view()),
    path('truck/', TruckList.as_view()),
]
