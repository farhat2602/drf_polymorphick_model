from django.urls import path

from services.views import ServiceCreate, ServiceList

urlpatterns = [
    path('service/create/', ServiceCreate.as_view()),
    path('services/', ServiceList.as_view()),
]
