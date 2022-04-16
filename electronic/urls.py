from django.urls import path
from electronic.views import (SmartphoneCreate, SmartphoneList, DialPhoneCreate, DialPhoneList,
                              TabletCreate, TabletList, DesktopCreate, DesktopList, LaptopCreate,
                              LaptopList, MonitorCreate, MonitorList, CameraCreate, CameraList,
                              SpeakerCreate, SpeakerList, HeadphoneCreate, HeadphoneList,
                              GameConsoleCreate, GameConsoleList, PrinterCreate, PrinterList)


urlpatterns = [
    path('smartphone/create/', SmartphoneCreate.as_view()),
    path('smartphone/', SmartphoneList.as_view()),
    path('dial_phone/create/', DialPhoneCreate.as_view()),
    path('dial_phone/', DialPhoneList.as_view()),
    path('tablet/create/', TabletCreate.as_view()),
    path('tablet/', TabletList.as_view()),
    path('desktop/create/', DesktopCreate.as_view()),
    path('desktop/', DesktopList.as_view()),
    path('laptop/create/', LaptopCreate.as_view()),
    path('laptop/', LaptopList.as_view()),
    path('monitor/create/', MonitorCreate.as_view()),
    path('monitor/', MonitorList.as_view()),
    path('camera/create/', CameraCreate.as_view()),
    path('camera/', CameraList.as_view()),
    path('speaker/create/', SpeakerCreate.as_view()),
    path('speaker/', SpeakerList.as_view()),
    path('headphone/create/', HeadphoneCreate.as_view()),
    path('headphone/', HeadphoneList.as_view()),
    path('game_console/create/', GameConsoleCreate.as_view()),
    path('game_console/', GameConsoleList.as_view()),
    path('printer/create/', PrinterCreate.as_view()),
    path('printer/', PrinterList.as_view()),
]
