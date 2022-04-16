from rest_framework import serializers
from home_garden.models import (Carpet, CarpetImage, ConsumerElectronic, ConsumerElectronicImage,
                                Furniture, FurnitureImage, Plant, PlantImage,
                                DishesAppliances, DishesAppliancesImage)


class CarpetImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarpetImage
        fields = '__all__'


class CarpetSerializer(serializers.ModelSerializer):
    images = CarpetImageSerializer(many=True, required=False)

    class Meta:
        model = Carpet
        fields = '__all__'


class ConsumerElectronicImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsumerElectronicImage
        fields = '__all__'


class ConsumerElectronicSerializer(serializers.ModelSerializer):
    images = ConsumerElectronicImageSerializer(many=True, required=False)

    class Meta:
        model = ConsumerElectronic
        fields = '__all__'


class FurnitureImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FurnitureImage
        fields = '__all__'


class FurnitureSerializer(serializers.ModelSerializer):
    images = FurnitureImageSerializer(many=True, required=False)

    class Meta:
        model = Furniture
        fields = '__all__'


class PlantImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantImage
        fields = '__all__'


class PlantSerializer(serializers.ModelSerializer):
    images = PlantImageSerializer(many=True, required=False)

    class Meta:
        model = Plant
        fields = '__all__'


class DishesAppliancesImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DishesAppliancesImage
        fields = '__all__'


class DishesAppliancesSerializer(serializers.ModelSerializer):
    images = DishesAppliancesImageSerializer(many=True, required=False)

    class Meta:
        model = DishesAppliances
        fields = '__all__'
