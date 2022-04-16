from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from home_garden.serializers import (CarpetSerializer, ConsumerElectronicSerializer, FurnitureSerializer,
                                     PlantSerializer, DishesAppliancesSerializer)
from home_garden.models import (Carpet, ConsumerElectronic, Furniture, Plant, DishesAppliances)


class CarpetCreate(generics.CreateAPIView):
    serializer_class = CarpetSerializer
    permission_classes = (IsAuthenticated, )


class CarpetList(generics.ListAPIView):
    queryset = Carpet.objects.all()
    serializer_class = CarpetSerializer


class ConsumerElectronicCreate(generics.CreateAPIView):
    serializer_class = ConsumerElectronicSerializer
    permission_classes = (IsAuthenticated, )


class ConsumerElectronicList(generics.ListAPIView):
    queryset = ConsumerElectronic.objects.all()
    serializer_class = ConsumerElectronicSerializer


class FurnitureCreate(generics.CreateAPIView):
    serializer_class = FurnitureSerializer
    permission_classes = (IsAuthenticated, )


class FurnitureList(generics.ListAPIView):
    queryset = Furniture.objects.all()
    serializer_class = FurnitureSerializer


class PlantCreate(generics.CreateAPIView):
    serializer_class = PlantSerializer
    permission_classes = (IsAuthenticated, )


class PlantList(generics.ListAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer


class DishesAppliancesCreate(generics.CreateAPIView):
    serializer_class = DishesAppliancesSerializer
    permission_classes = (IsAuthenticated, )


class DishesAppliancesList(generics.ListAPIView):
    queryset = DishesAppliances.objects.all()
    serializer_class = DishesAppliancesSerializer
