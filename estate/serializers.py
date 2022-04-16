from rest_framework import serializers
from estate.models import(Estate, Apartment, ApartmentImage, Office, OfficeImage,
                          CottageHouse, CottageHouseImage, LandPlot,
                          LandPlotImage, WorkPlace, WorkPlaceImage)


class EstateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estate
        fields = '__all__'


class ApartmentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentImage
        fields = '__all__'


class ApartmentSerializer(serializers.ModelSerializer):

    images = ApartmentImageSerializer(many=True, required=False)

    class Meta:
        model = Apartment
        fields = '__all__'


class OfficeImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfficeImage
        fields = '__all__'


class OfficeSerializer(serializers.ModelSerializer):

    images = OfficeImageSerializer(many=True, required=False)

    class Meta:
        model = Office
        fields = '__all__'


class CottageHouseImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CottageHouseImage
        fields = '__all__'


class CottageHouseSerializer(serializers.ModelSerializer):

    images = CottageHouseImageSerializer(many=True, required=False)

    class Meta:
        model = CottageHouse
        fields = '__all__'


class LandPlotImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandPlotImage
        fields = '__all__'


class LandPlotSerializer(serializers.ModelSerializer):

    images = LandPlotImageSerializer(many=True, required=False)

    class Meta:
        model = LandPlot
        fields = '__all__'


class WorkPlaceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkPlaceImage
        fields = '__all__'


class WorkPlaceSerializer(serializers.ModelSerializer):

    images = WorkPlaceImageSerializer(many=True, required=False)

    class Meta:
        model = WorkPlace
        fields = '__all__'
