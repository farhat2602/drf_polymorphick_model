from django.contrib import admin
from electronic.models import (Smartphone, SmartphoneImage, DialPhone,
                               DialPhoneImage, Tablet, TabletImage, Desktop, DesktopImage,
                               Laptop, LaptopImage, Monitor, MonitorImage)


class SmartphoneImageInline(admin.StackedInline):
    model = SmartphoneImage

@admin.register(Smartphone)
class SmartphoneAdmin(admin.ModelAdmin):
    inlines = [SmartphoneImageInline]
    list_display = ['title', 'brand_type', 'owner', 'price', 'is_published']


class ClassicPhoneImageInline(admin.StackedInline):
    model = DialPhoneImage

@admin.register(DialPhone)
class ClassicPhoneAdmin(admin.ModelAdmin):
    inlines = [ClassicPhoneImageInline]
    list_display = ['title', 'brand_type', 'owner', 'price', 'is_published']


class TabletImageInline(admin.StackedInline):
    model = TabletImage

@admin.register(Tablet)
class TabletAdmin(admin.ModelAdmin):
    inlines = [TabletImageInline]
    list_display = ['title', 'brand_type', 'owner', 'price', 'is_published']


class DesktopImageInline(admin.StackedInline):
    model = DesktopImage

@admin.register(Desktop)
class DesktopAdmin(admin.ModelAdmin):
    inlines = [DesktopImageInline]
    list_display = ['title', 'brand_type', 'owner', 'price', 'is_published']


class LaptopImageInline(admin.StackedInline):
    model = LaptopImage

@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    inlines = [LaptopImageInline]
    list_display = ['title', 'brand_type', 'owner', 'price', 'is_published']


class MonitorImageInline(admin.StackedInline):
    model = MonitorImage

@admin.register(Monitor)
class SmartwatchAdmin(admin.ModelAdmin):
    inlines = [MonitorImageInline]
    list_display = ['title', 'brand_type', 'owner', 'price', 'is_published']

