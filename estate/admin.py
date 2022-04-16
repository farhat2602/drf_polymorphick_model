from django.contrib import admin
from estate.models import (Apartment, ApartmentImage, Office, OfficeImage,
                           CottageHouse, CottageHouseImage, LandPlot,
                           LandPlotImage, WorkPlace, WorkPlaceImage)


class ApartmentImageInline(admin.StackedInline):
    model = ApartmentImage

@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    inlines = [ApartmentImageInline]
    list_display = ['title', 'owner', 'price', 'is_published']


class OfficeImageInline(admin.StackedInline):
    model = OfficeImage

@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    inlines = [OfficeImageInline]
    list_display = ['title', 'owner', 'price', 'is_published']


class CottageHouseImageInline(admin.StackedInline):
    model = CottageHouseImage

@admin.register(CottageHouse)
class CottageHouseAdmin(admin.ModelAdmin):
    inlines = [CottageHouseImageInline]
    list_display = ['title', 'owner', 'price', 'is_published']


class LandPlotImageInline(admin.StackedInline):
    model = LandPlotImage

@admin.register(LandPlot)
class LandPlotAdmin(admin.ModelAdmin):
    inlines = [LandPlotImageInline]
    list_display = ['title', 'owner', 'price', 'is_published']


class WorkPlaceImageInline(admin.StackedInline):
    model = WorkPlaceImage

@admin.register(WorkPlace)
class WorkPlaceAdmin(admin.ModelAdmin):
    inlines = [WorkPlaceImageInline]
    list_display = ['title', 'owner', 'price', 'is_published']

