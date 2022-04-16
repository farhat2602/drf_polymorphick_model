from PIL import Image
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
from django.db import models
from model_utils.fields import StatusField
from model_utils import Choices
from post.models import Post


User = get_user_model()


class Estate(Post):

    sell_choice = Choices('Sell', 'Rent')
    sell_type = StatusField(choices_name='sell_choice')

    def __str__(self):
        return str(self.sell_type)


class Apartment(Estate):

    room = models.IntegerField(null=True, blank=True)
    floor_choice = Choices('1', '2', '3', '4', '5', '6', '7', '8', '9', '9+')
    floor_type = StatusField(choices_name='floor_choice')
    square = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])

    def __str__(self):
        return str(self.pk)


class ApartmentImage(models.Model):

    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name='apartment_images')
    images = models.ImageField(upload_to='estate/apartment_images/', null=True, blank=True)


class Office(Estate):

    room = models.IntegerField(null=True, blank=True)
    floor_choice = Choices('1', '2', '3', '4', '5', '6', '7', '8', '9', '9+')
    floor_type = StatusField(choices_name='floor_choice')
    square = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])

    def __str__(self):
        return str(self.pk)


class OfficeImage(models.Model):

    office = models.ForeignKey(Office, on_delete=models.CASCADE, related_name='office_images')
    images = models.ImageField(upload_to='estate/office_images/', null=True, blank=True)


class CottageHouse(Estate):

    room = models.IntegerField(null=True, blank=True)
    floor_choice = Choices('1', '2', '3', '4', '5', '6', '7', '8', '9', '9+')
    floor_type = StatusField(choices_name='floor_choice')
    square = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    square_choice = Choices('M2', 'SOT', 'GA')
    square_type = StatusField(choices_name='square_choice')

    def __str__(self):
        return str(self.pk)


class CottageHouseImage(models.Model):

    cottage_house = models.ForeignKey(CottageHouse, on_delete=models.CASCADE, related_name='cottage_house_images')
    images = models.ImageField(upload_to='estate/cottage_house_images/', null=True, blank=True)


class LandPlot(Estate):

    square = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    square_choice = Choices('M2', 'SOT', 'GA')
    square_type = StatusField(choices_name='square_choice')

    def __str__(self):
        return str(self.pk)


class LandPlotImage(models.Model):

    land_plot = models.ForeignKey(LandPlot, on_delete=models.CASCADE, related_name='land_plot_images')
    images = models.ImageField(upload_to='estate/land_plot_images/', null=True, blank=True)


class WorkPlace(Estate):

    room = models.IntegerField(null=True, blank=True)
    floor_choice = Choices('1', '2', '3', '4', '5', '6', '7', '8', '9', '9+')
    floor_type = StatusField(choices_name='floor_choice')
    square = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    square_choice = Choices('M2', 'SOT', 'GA')
    square_type = StatusField(choices_name='square_choice')

    def __str__(self):
        return str(self.pk)


class WorkPlaceImage(models.Model):

    workplace = models.ForeignKey(WorkPlace, on_delete=models.CASCADE, related_name='workplace_images')
    images = models.ImageField(upload_to='estate/workplace_images/', null=True, blank=True)
