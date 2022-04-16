from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from fashion.models import (ManClothes, WomanClothes, ChildClothes, Watch, Shoes, Underwear,
                            Bag, Cosmetic, Accessories, Textile)
from fashion.serializers import (ManClothesSerializer, WomanClothesSerializer, ChildClothesSerializer,
                                 WatchSerializer, ShoesSerializer, UnderwearSerializer, BagSerializer,
                                 CosmeticSerializer, AccessoriesSerializer, TextileSerializer)


class ManClothesCreate(generics.CreateAPIView):
    serializer_class = ManClothesSerializer
    permission_classes = (IsAuthenticated, )


class ManClothesList(generics.ListAPIView):
    queryset = ManClothes.objects.all()
    serializer_class = ManClothesSerializer


class WomanClothesCreate(generics.CreateAPIView):
    serializer_class = WomanClothesSerializer
    permission_classes = (IsAuthenticated, )


class WomanClothesList(generics.ListAPIView):
    queryset = WomanClothes.objects.all()
    serializer_class = WomanClothesSerializer


class ChildClothesCreate(generics.CreateAPIView):
    serializer_class = ChildClothesSerializer
    permission_classes = (IsAuthenticated, )


class ChildClothesList(generics.ListAPIView):
    queryset = ChildClothes.objects.all()
    serializer_class = ChildClothesSerializer


class WatchCreate(generics.CreateAPIView):
    serializer_class = WatchSerializer
    permission_classes = (IsAuthenticated, )


class WatchList(generics.ListAPIView):
    queryset = Watch.objects.all()
    serializer_class = WatchSerializer


class ShoesCreate(generics.CreateAPIView):
    serializer_class = ShoesSerializer
    permission_classes = (IsAuthenticated, )


class ShoesList(generics.ListAPIView):
    queryset = Shoes.objects.all()
    serializer_class = ShoesSerializer


class UnderwearCreate(generics.CreateAPIView):
    serializer_class = UnderwearSerializer
    permission_classes = (IsAuthenticated, )


class UnderwearList(generics.ListAPIView):
    queryset = Underwear.objects.all()
    serializer_class = UnderwearSerializer


class BagCreate(generics.CreateAPIView):
    serializer_class = BagSerializer
    permission_classes = (IsAuthenticated, )


class BagList(generics.ListAPIView):
    queryset = Bag.objects.all()
    serializer_class = BagSerializer


class CosmeticCreate(generics.CreateAPIView):
    serializer_class = CosmeticSerializer
    permission_classes = (IsAuthenticated, )


class CosmeticList(generics.ListAPIView):
    queryset = Cosmetic.objects.all()
    serializer_class = CosmeticSerializer


class AccessoriesCreate(generics.CreateAPIView):
    serializer_class = AccessoriesSerializer
    permission_classes = (IsAuthenticated, )


class AccessoriesList(generics.ListAPIView):
    queryset = Accessories.objects.all()
    serializer_class = AccessoriesSerializer


class TextileCreate(generics.CreateAPIView):
    serializer_class = TextileSerializer
    permission_classes = (IsAuthenticated, )


class TextileList(generics.ListAPIView):
    queryset = Textile.objects.all()
    serializer_class = TextileSerializer
