from django.urls import path
from fashion.views import (ManClothesCreate, ManClothesList, WomanClothesCreate, WomanClothesList,
                           ChildClothesCreate, ChildClothesList, WatchCreate, WatchList,
                           ShoesCreate, ShoesList, UnderwearCreate, UnderwearList, BagCreate,
                           BagList, CosmeticCreate, CosmeticList, AccessoriesCreate,
                           AccessoriesList, TextileCreate, TextileList)

urlpatterns = [
    path('man_clothes/create/', ManClothesCreate.as_view()),
    path('man_clothes/', ManClothesList.as_view()),
    path('woman_clothes/create/', WomanClothesCreate.as_view()),
    path('woman_clothes/', WomanClothesList.as_view()),
    path('child_clothes/create/', ChildClothesCreate.as_view()),
    path('child_clothes/', ChildClothesList.as_view()),
    path('watch/create/', WatchCreate.as_view()),
    path('watch/', WatchList.as_view()),
    path('shoes/create/', ShoesCreate.as_view()),
    path('shoes/', ShoesList.as_view()),
    path('underwear/create/', UnderwearCreate.as_view()),
    path('underwear/', UnderwearList.as_view()),
    path('bag/create/', BagCreate.as_view()),
    path('bag/', BagList.as_view()),
    path('cosmetic/create/', CosmeticCreate.as_view()),
    path('cosmetic/', CosmeticList.as_view()),
    path('accessories/create/', AccessoriesCreate.as_view()),
    path('accessories/', AccessoriesList.as_view()),
    path('textile/create/', TextileCreate.as_view()),
    path('textile/', TextileList.as_view()),
]
