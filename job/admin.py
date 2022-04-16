from django.contrib import admin
from job.models import (Vacancy, VacancyImage, Resume, ResumeImage)


class VacancyImageInline(admin.StackedInline):
    model = VacancyImage


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    inlines = [VacancyImageInline]
    list_display = ['title', 'owner', 'is_published']


class ResumeImageInline(admin.StackedInline):
    model = ResumeImage


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    inlines = [ResumeImageInline]
    list_display = ['title', 'owner', 'is_published']
