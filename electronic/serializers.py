from rest_framework import serializers
from electronic.models import (Electronic, Smartphone, SmartphoneImage,
                               DialPhone, DialPhoneImage, Tablet, TabletImage,
                               Desktop, DesktopImage, Laptop, LaptopImage,
                               Monitor, MonitorImage, Camera, CameraImage,
                               Speaker, SpeakerImage, Headphone, HeadphoneImage,
                               GameConsole, GameConsoleImage, Printer, PrinterImage)


class ElectronicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Electronic
        fields = '__all__'


class SmartphoneImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmartphoneImage
        fields = '__all__'


class SmartphoneSerializer(serializers.ModelSerializer):
    images = SmartphoneImageSerializer(many=True, required=False)

    class Meta:
        model = Smartphone
        fields = '__all__'


class DialPhoneImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DialPhoneImage
        fields = '__all__'


class DialPhoneSerializer(serializers.ModelSerializer):
    images = DialPhoneImageSerializer(many=True, required=False)

    class Meta:
        model = DialPhone
        fields = '__all__'


class TabletImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TabletImage
        fields = '__all__'


class TabletSerializer(serializers.ModelSerializer):
    images = TabletImageSerializer(many=True, required=False)

    class Meta:
        model = Tablet
        fields = '__all__'


class DesktopImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DesktopImage
        fields = '__all__'


class DesktopSerializer(serializers.ModelSerializer):
    images = DesktopImageSerializer(many=True, required=False)

    class Meta:
        model = Desktop
        fields = '__all__'


class LaptopImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaptopImage
        fields = '__all__'


class LaptopSerializer(serializers.ModelSerializer):
    images = LaptopImageSerializer(many=True, required=False)

    class Meta:
        model = Laptop
        fields = '__all__'


class MonitorImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitorImage
        fields = '__all__'


class MonitorSerializer(serializers.ModelSerializer):
    images = MonitorImageSerializer(many=True, required=False)

    class Meta:
        model = Monitor
        fields = '__all__'


class CameraImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CameraImage
        fields = '__all__'


class CameraSerializer(serializers.ModelSerializer):
    images = CameraImageSerializer(many=True, required=False)

    class Meta:
        model = Camera
        fields = '__all__'


class SpeakerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpeakerImage
        fields = '__all__'


class SpeakerSerializer(serializers.ModelSerializer):
    images = SpeakerImageSerializer(many=True, required=False)

    class Meta:
        model = Speaker
        fields = '__all__'


class HeadphoneImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeadphoneImage
        fields = '__all__'


class HeadphoneSerializer(serializers.ModelSerializer):
    images = HeadphoneImageSerializer(many=True, required=False)

    class Meta:
        model = Headphone
        fields = '__all__'


class GameConsoleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameConsoleImage
        fields = '__all__'


class GameConsoleSerializer(serializers.ModelSerializer):
    images = GameConsoleImageSerializer(many=True, required=False)

    class Meta:
        model = GameConsole
        fields = '__all__'


class PrinterImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrinterImage
        fields = '__all__'


class PrinterSerializer(serializers.ModelSerializer):
    images = PrinterImageSerializer(many=True, required=False)

    class Meta:
        model = Printer
        fields = '__all__'
