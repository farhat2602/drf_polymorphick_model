from django.contrib import admin
from transport.models import (Car, CarImage,
                              Motorcycle, MotorcycleImage, Truck, TruckImage)


class CarImageInline(admin.StackedInline):
    model = CarImage


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    inlines = [CarImageInline]
    list_display = ['title', 'brand_type', 'owner', 'price', 'is_published']


class MotorcycleImageInline(admin.StackedInline):
    model = MotorcycleImage


@admin.register(Motorcycle)
class MotorcycleAdmin(admin.ModelAdmin):
    inlines = [MotorcycleImageInline]
    list_display = ['title', 'brand_type', 'owner', 'price', 'is_published']


class TruckImageInline(admin.StackedInline):
    model = TruckImage


@admin.register(Truck)
class TruckAdmin(admin.ModelAdmin):
    inlines = [TruckImageInline]
    list_display = ['title', 'brand_type', 'owner', 'price', 'is_published']
