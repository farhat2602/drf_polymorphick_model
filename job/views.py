from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from job.models import Vacancy, Resume
from job.serializers import VacancySerializer, ResumeSerializer


class VacancyCreate(generics.CreateAPIView):
    serializer_class = VacancySerializer
    permission_classes = (IsAuthenticated, )


class VacancyList(generics.ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer


class ResumeCreate(generics.CreateAPIView):
    serializer_class = ResumeSerializer
    permission_classes = (IsAuthenticated, )


class ResumeList(generics.ListAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
