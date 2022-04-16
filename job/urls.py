from django.urls import path

from job.views import VacancyCreate, VacancyList, ResumeCreate, ResumeList


urlpatterns = [
    path('vacancy/create/', VacancyCreate.as_view()),
    path('vacancies/', VacancyList.as_view()),
    path('resume/create/', ResumeCreate.as_view()),
    path('resumes/', ResumeList.as_view()),
]
