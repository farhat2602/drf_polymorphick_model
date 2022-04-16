from rest_framework import serializers

from services.models import Service, ServiceImage


class ServiceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceImage
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    images = ServiceImageSerializer(many=True, required=False)

    class Meta:
        model = Service
        fields = '__all__'
