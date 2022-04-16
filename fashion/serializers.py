from rest_framework import serializers
from fashion.models import (ManClothes, ManClothesImage, WomanClothes, WomanClothesImage,
                            ChildClothes, ChildClothesImage, Watch, WatchImage, Shoes, ShoesImage,
                            Underwear, UnderwearImage, Bag, BagImage, Cosmetic, CosmeticImage,
                            Accessories, AccessoriesImage, Textile, TextileImage)


class ManClothesImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManClothesImage
        fields = '__all__'


class ManClothesSerializer(serializers.ModelSerializer):
    images = ManClothesImageSerializer(many=True, required=False)

    class Meta:
        model = ManClothes
        fields = '__all__'


class WomanClothesImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WomanClothesImage
        fields = '__all__'


class WomanClothesSerializer(serializers.ModelSerializer):
    images = WomanClothesImageSerializer(many=True, required=False)

    class Meta:
        model = WomanClothes
        fields = '__all__'


class ChildClothesImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChildClothesImage
        fields = '__all__'


class ChildClothesSerializer(serializers.ModelSerializer):
    images = ChildClothesImageSerializer(many=True, required=False)

    class Meta:
        model = ChildClothes
        fields = '__all__'


class WatchImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchImage
        fields = '__all__'


class WatchSerializer(serializers.ModelSerializer):
    images = WatchImageSerializer(many=True, required=False)

    class Meta:
        model = Watch
        fields = '__all__'


class ShoesImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoesImage
        fields = '__all__'


class ShoesSerializer(serializers.ModelSerializer):
    images = ShoesImageSerializer(many=True, required=False)

    class Meta:
        model = Shoes
        fields = '__all__'


class UnderwearImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnderwearImage
        fields = '__all__'


class UnderwearSerializer(serializers.ModelSerializer):
    images = UnderwearImageSerializer(many=True, required=False)

    class Meta:
        model = Underwear
        fields = '__all__'


class BagImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BagImage
        fields = '__all__'


class BagSerializer(serializers.ModelSerializer):
    images = BagImageSerializer(many=True, required=False)

    class Meta:
        model = Bag
        fields = '__all__'


class CosmeticImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CosmeticImage
        fields = '__all__'


class CosmeticSerializer(serializers.ModelSerializer):
    images = CosmeticImageSerializer(many=True, required=False)

    class Meta:
        model = Cosmetic
        fields = '__all__'


class AccessoriesImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessoriesImage
        fields = '__all__'


class AccessoriesSerializer(serializers.ModelSerializer):
    images = AccessoriesImageSerializer(many=True, required=False)

    class Meta:
        model = Accessories
        fields = '__all__'


class TextileImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextileImage
        fields = '__all__'


class TextileSerializer(serializers.ModelSerializer):
    images = TextileImageSerializer(many=True, required=False)

    class Meta:
        model = Textile
        fields = '__all__'
        