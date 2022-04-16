from django.db import models
from model_utils import Choices
from model_utils.fields import StatusField

from post.models import Post


class ManClothes(Post):

    clothes_choice = Choices('Tshirt', 'Shirt', 'SweatShirt', 'Classic Suit', 'Jacket', 'Shorts', 'Pant',
                             'Jeans', 'JeansJacket', 'Coat', 'SportWear')
    clothes_type = StatusField(choices_name='clothes_choice')
    size_choice = Choices('XS', 'S', 'M', 'L', 'XL', 'XXL', '3XL', '4XL', '5XL')
    size_type = StatusField(choices_name='size_choice')

    def __str__(self):
        return self.clothes_type


class ManClothesImage(models.Model):
    man_clothes = models.ForeignKey(ManClothes, on_delete=models.CASCADE, related_name='images')
    images = models.ImageField(upload_to='fashion/man_clothes_images/')


class WomanClothes(Post):

    clothes_choice = Choices('Tshirt', 'Shirt', 'Skirt', 'Blouse', 'Dress', 'SweatShirt', 'Classic Suit', 'Jacket',
                             'Shorts', 'Pant', 'Jeans', 'JeansJacket', 'Coat', 'SportWear')
    clothes_type = StatusField(choices_name='clothes_choice')
    size_choice = Choices('XS', 'S', 'M', 'L', 'XL', 'XXL', '3XL', '4XL', '5XL')
    size_type = StatusField(choices_name='size_choice')

    def __str__(self):
        return self.clothes_type


class WomanClothesImage(models.Model):
    woman_clothes = models.ForeignKey(WomanClothes, on_delete=models.CASCADE, related_name='images')
    images = models.ImageField(upload_to='fashion/woman_clothes_images/')


class ChildClothes(Post):

    clothes_choice = Choices('Tshirt', 'Shirt', 'Skirt', 'Blouse', 'Dress', 'SweatShirt', 'Classic Suit', 'Jacket',
                             'Shorts', 'Pant',
                             'Jeans', 'JeansJacket', 'Coat', 'SportWear')
    clothes_type = StatusField(choices_name='clothes_choice')
    size_choice = Choices('1-3 month', '3-5 month', '5-7 month', '8-10 month', '1 year',
                          '2-3 year', '4-5 year', '6-7 year', '8-10 year')
    size_type = StatusField(choices_name='size_choice')

    def __str__(self):
        return self.clothes_type


class ChildClothesImage(models.Model):
    child_clothes = models.ForeignKey(ChildClothes, on_delete=models.CASCADE, related_name='images')
    images = models.ImageField(upload_to='fashion/child_clothes_images/')


class Watch(Post):

    gender_choice = Choices('Unisex', 'Man', 'Woman', 'Child')
    gender_type = StatusField(choices_name='gender_choice')
    watch_choice = Choices('Smart', 'Mechanic')
    watch_type = StatusField(choices_name='watch_choice')
    state_choice = Choices('New', '2Hand')
    state_type = StatusField(choices_name='state_choice')

    def __str__(self):
        return self.gender_type


class WatchImage(models.Model):
    watch = models.ForeignKey(Watch, on_delete=models.CASCADE, related_name='images')
    images = models.ImageField(upload_to='fashion/watch_images/')


class Shoes(Post):

    gender_choice = Choices('Man', 'Woman', 'Child')
    gender_type = StatusField(choices_name='gender_choice')
    shoes_choice = Choices('Daily', 'Sport', 'Classic', 'Sandals', 'Outdoor')
    shoes_type = StatusField(choices_name='shoes_choice')

    def __str__(self):
        return self.gender_type


class ShoesImage(models.Model):
    shoes = models.ForeignKey(Shoes, on_delete=models.CASCADE, related_name='images')
    images = models.ImageField(upload_to='fashion/shoes_images/')


class Underwear(Post):

    gender_choice = Choices('Man', 'Woman', 'Child')
    gender_type = StatusField(choices_name='gender_choice')

    def __str__(self):
        return self.gender_type


class UnderwearImage(models.Model):
    underwear = models.ForeignKey(Underwear, on_delete=models.CASCADE, related_name='images')
    images = models.ImageField(upload_to='fashion/underwear_images/')


class Bag(Post):

    gender_choice = Choices('Unisex', 'Man', 'Woman', 'Child')
    gender_type = StatusField(choices_name='gender_choice')

    def __str__(self):
        return self.gender_type


class BagImage(models.Model):
    bag = models.ForeignKey(Bag, on_delete=models.CASCADE, related_name='images')
    images = models.ImageField(upload_to='fashion/bag_images/')


class Cosmetic(Post):

    gender_choice = Choices('Unisex', 'Man', 'Woman', 'Child')
    gender_type = StatusField(choices_name='gender_choice')

    def __str__(self):
        return self.gender_type


class CosmeticImage(models.Model):
    cosmetic = models.ForeignKey(Cosmetic, on_delete=models.CASCADE, related_name='images')
    images = models.ImageField(upload_to='fashion/cosmetic_images/')


class Accessories(Post):

    gender_choice = Choices('Unisex', 'Man', 'Woman', 'Child')
    gender_type = StatusField(choices_name='gender_choice')

    def __str__(self):
        return self.gender_type


class AccessoriesImage(models.Model):
    accessories = models.ForeignKey(Accessories, on_delete=models.CASCADE, related_name='images')
    images = models.ImageField(upload_to='fashion/accessories_images/')


class Textile(Post):

    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class TextileImage(models.Model):
    accessories = models.ForeignKey(Textile, on_delete=models.CASCADE, related_name='images')
    images = models.ImageField(upload_to='fashion/textile_images/')
