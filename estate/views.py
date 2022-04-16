from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from estate.serializers import (ApartmentSerializer, OfficeSerializer, CottageHouseSerializer,
                                LandPlotSerializer, WorkPlaceSerializer)
from estate.models import Apartment, Office, CottageHouse, LandPlot, WorkPlace


class ApartmentCreate(generics.CreateAPIView):
    serializer_class = ApartmentSerializer
    permission_classes = (IsAuthenticated, )


class ApartmentList(generics.ListAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer


class OfficeCreate(generics.CreateAPIView):
    serializer_class = OfficeSerializer
    permission_classes = (IsAuthenticated, )


class OfficeList(generics.ListAPIView):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer


class CottageHouseCreate(generics.CreateAPIView):
    serializer_class = CottageHouseSerializer
    permission_classes = (IsAuthenticated, )


class CottageHouseList(generics.ListAPIView):

    queryset = CottageHouse.objects.all()
    serializer_class = CottageHouseSerializer


class LandPlotCreate(generics.CreateAPIView):
    serializer_class = LandPlotSerializer
    permission_classes = (IsAuthenticated, )


class LandPlotList(generics.ListAPIView):
    queryset = LandPlot.objects.all()
    serializer_class = LandPlotSerializer


class WorkPlaceCreate(generics.CreateAPIView):
    serializer_class = WorkPlaceSerializer
    permission_classes = (IsAuthenticated, )


class WorkPlaceList(generics.ListAPIView):
    queryset = WorkPlace.objects.all()
    serializer_class = WorkPlaceSerializer
