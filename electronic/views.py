from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from electronic.models import (Smartphone, DialPhone, Tablet, Desktop, Laptop, Monitor, Camera,
                               Speaker, Headphone, GameConsole, Printer)
from electronic.serializers import (SmartphoneSerializer, DialPhoneSerializer, TabletSerializer,
                                    DesktopSerializer,  LaptopSerializer, MonitorSerializer,
                                    CameraSerializer, SpeakerSerializer, HeadphoneSerializer,
                                    GameConsoleSerializer, PrinterSerializer)


class SmartphoneCreate(generics.CreateAPIView):
    serializer_class = SmartphoneSerializer
    permission_classes = (IsAuthenticated, )


class SmartphoneList(generics.ListAPIView):

    queryset = Smartphone.objects.all()
    serializer_class = SmartphoneSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['brand_type', 'price']


class DialPhoneCreate(generics.CreateAPIView):
    serializer_class = DialPhoneSerializer
    permission_classes = (IsAuthenticated, )


class DialPhoneList(generics.ListAPIView):

    queryset = DialPhone.objects.all()
    serializer_class = DialPhoneSerializer


class TabletCreate(generics.CreateAPIView):
    serializer_class = TabletSerializer
    permission_classes = (IsAuthenticated, )


class TabletList(generics.ListAPIView):

    queryset = Tablet.objects.all()
    serializer_class = TabletSerializer


class DesktopCreate(generics.CreateAPIView):
    serializer_class = DesktopSerializer
    permission_classes = (IsAuthenticated, )


class DesktopList(generics.ListAPIView):

    queryset = Desktop.objects.all()
    serializer_class = DesktopSerializer


class LaptopCreate(generics.CreateAPIView):
    serializer_class = LaptopSerializer
    permission_classes = (IsAuthenticated, )


class LaptopList(generics.ListAPIView):

    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer


class MonitorCreate(generics.CreateAPIView):
    serializer_class = MonitorSerializer
    permission_classes = (IsAuthenticated, )


class MonitorList(generics.ListAPIView):

    queryset = Monitor.objects.all()
    serializer_class = MonitorSerializer


class CameraCreate(generics.CreateAPIView):
    serializer_class = CameraSerializer
    permission_classes = (IsAuthenticated, )


class CameraList(generics.ListAPIView):

    queryset = Camera.objects.all()
    serializer_class = CameraSerializer


class SpeakerCreate(generics.CreateAPIView):
    serializer_class = SpeakerSerializer
    permission_classes = (IsAuthenticated, )


class SpeakerList(generics.ListAPIView):

    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer


class HeadphoneCreate(generics.CreateAPIView):
    serializer_class = HeadphoneSerializer
    permission_classes = (IsAuthenticated, )


class HeadphoneList(generics.ListAPIView):

    queryset = Headphone.objects.all()
    serializer_class = HeadphoneSerializer


class GameConsoleCreate(generics.CreateAPIView):
    serializer_class = GameConsoleSerializer
    permission_classes = (IsAuthenticated, )


class GameConsoleList(generics.ListAPIView):

    queryset = GameConsole.objects.all()
    serializer_class = GameConsoleSerializer


class PrinterCreate(generics.CreateAPIView):
    serializer_class = PrinterSerializer
    permission_classes = (IsAuthenticated, )


class PrinterList(generics.ListAPIView):

    queryset = Printer.objects.all()
    serializer_class = PrinterSerializer
