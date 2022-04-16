from django.urls import path

from home_garden.views import (CarpetCreate, CarpetList, ConsumerElectronicCreate, ConsumerElectronicList,
                               FurnitureCreate, FurnitureList,  PlantCreate, PlantList,
                               DishesAppliancesCreate, DishesAppliancesList)


urlpatterns = [
    path('carpet/create/', CarpetCreate.as_view()),
    path('carpets/', CarpetList.as_view()),
    path('consumer_electronic/create/', ConsumerElectronicCreate.as_view()),
    path('consumer_electronics/', ConsumerElectronicList.as_view()),
    path('furniture/create/', FurnitureCreate.as_view()),
    path('furniture/', FurnitureList.as_view()),
    path('plant/create/', PlantCreate.as_view()),
    path('plants/', PlantList.as_view()),
    path('dishes_appliances/create/', DishesAppliancesCreate.as_view()),
    path('dishes_appliances/', DishesAppliancesList.as_view()),
]