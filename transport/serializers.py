from rest_framework import serializers
from transport.models import (Transport, Car, CarImage, Motorcycle, MotorcycleImage, Truck, TruckImage)


class TransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transport
        fields = '__all__'


class CarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImage
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    images = CarImageSerializer(many=True, required=False)

    class Meta:
        model = Car
        fields = '__all__'


class MotorcycleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotorcycleImage
        fields = '__all__'


class MotorcycleSerializer(serializers.ModelSerializer):
    images = MotorcycleImageSerializer(many=True, required=False)

    class Meta:
        model = Motorcycle
        fields = '__all__'


class TruckImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TruckImage
        fields = '__all__'


class TruckSerializer(serializers.ModelSerializer):
    images = TruckImageSerializer(many=True, required=False)

    class Meta:
        model = Truck
        fields = '__all__'
