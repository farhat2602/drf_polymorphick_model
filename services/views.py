from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from services.models import Service
from services.serializers import ServiceSerializer


class ServiceCreate(generics.CreateAPIView):
    serializer_class = ServiceSerializer
    permission_classes = (IsAuthenticated, )


class ServiceList(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
