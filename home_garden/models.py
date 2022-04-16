from django.db import models
from model_utils import Choices
from model_utils.fields import StatusField

from post.models import Post


class Carpet(Post):

    made_choice = Choices('Handmade', 'Machine')
    made_type = StatusField(choices_name='made_choice')

    def __str__(self):
        return self.made_type


class CarpetImage(models.Model):
    carpet = models.ForeignKey(Carpet, on_delete=models.CASCADE, related_name='carpet_images')
    images = models.ImageField(upload_to='home_garden/carpet_images/')


class ConsumerElectronic(Post):

    consumer_choice = Choices('TV', 'Security Camera', 'Vacuum Cleaners', 'Refrigerator', 'Freezer',
                            'Oven', 'Microwave', 'Toaster', 'DishWasher', 'Washing Machine', 'Dryer',
                            'Coffee Maker', 'Blender', 'Mixer', 'Iron', 'Conditioner', 'Other')
    consumer_type = StatusField(choices_name='consumer_choice')

    def __str__(self):
        return self.consumer_type


class ConsumerElectronicImage(models.Model):
    consumer_electronic = models.ForeignKey(ConsumerElectronic, on_delete=models.CASCADE, related_name='cons_images')
    images = models.ImageField(upload_to='home_garden/consumer_e_images/')


class Furniture(Post):

    furniture_choice = Choices('Bed', 'Sofas', 'Armchair', 'Cabinet', 'Table', 'Shelving', 'Chair',
                               'Stand', 'Computer Table', 'Kitchen Set', 'Book Case', 'Bedside Table', 'Other')
    furniture_type = StatusField(choices_name='furniture_choice')

    def __str__(self):
        return self.furniture_type


class FurnitureImage(models.Model):
    furniture = models.ForeignKey(Furniture, on_delete=models.CASCADE, related_name='furniture_images')
    images = models.ImageField(upload_to='home_garden/furniture_images/')


class Plant(Post):

    plant_type = models.CharField(max_length=55)

    def __str__(self):
        return self.plant_type


class PlantImage(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='plant_images')
    images = models.ImageField(upload_to='home_garden/plant_images/')


class DishesAppliances(Post):

    good_choice = Choices('Dish', 'Appliance')
    good_type = StatusField(choices_name='good_choice')

    def __str__(self):
        return self.good_type


class DishesAppliancesImage(models.Model):
    dishes = models.ForeignKey(DishesAppliances, on_delete=models.CASCADE, related_name='dishes_images')
    images = models.ImageField(upload_to='home_garden/dishes_images/')
