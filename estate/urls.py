from django.urls import path
from estate.views import (ApartmentCreate, ApartmentList, OfficeCreate, OfficeList,
                          CottageHouseCreate, CottageHouseList, LandPlotCreate,
                          LandPlotList, WorkPlaceCreate, WorkPlaceList)


urlpatterns = [
    path('apartment/create/', ApartmentCreate.as_view()),
    path('apartment/', ApartmentList.as_view()),
    path('office/create/', OfficeCreate.as_view()),
    path('office/', OfficeList.as_view()),
    path('cottage_house/create/', CottageHouseCreate.as_view()),
    path('cottage_house/', CottageHouseList.as_view()),
    path('land_plot/create/', LandPlotCreate.as_view()),
    path('land_plot/', LandPlotList.as_view()),
    path('workplace/create/', WorkPlaceCreate.as_view()),
    path('workplace/', WorkPlaceList.as_view()),
]
