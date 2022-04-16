from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from root_config.permissions import IsOwnerOrReadOnly
from transport.serializers import (CarSerializer, MotorcycleSerializer, TruckSerializer)
from transport.models import Car, Motorcycle, Truck


class CarCreate(generics.CreateAPIView):
    serializer_class = CarSerializer
    permission_classes = (IsAuthenticated, )


class CarList(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class MotorcycleCreate(generics.CreateAPIView):
    serializer_class = MotorcycleSerializer
    permission_classes = (IsAuthenticated, )


class MotorcycleList(generics.ListAPIView):

    queryset = Motorcycle.objects.all()
    serializer_class = MotorcycleSerializer


class TruckCreate(generics.CreateAPIView):
    serializer_class = TruckSerializer
    permission_classes = (IsAuthenticated, )


class TruckList(generics.ListAPIView):
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer
