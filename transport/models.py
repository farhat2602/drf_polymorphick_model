from PIL import Image
from django.core.validators import MaxValueValidator
from django.db import models
from django.contrib.auth import get_user_model
from model_utils import Choices
from model_utils.fields import StatusField

from post.models import Post

User = get_user_model()


class Transport(Post):

    brand_choice = Choices('Audi', 'BMW', 'Chery', 'Chevrolet', 'Citroen', 'Chrysler', 'DAF',
                           'Daewoo', 'Dodge', 'Ford', 'Forland', 'Fekon', 'Fiat', 'Geely',
                           'Honda', 'Howo', 'Hyundai', 'Infiniti', 'Iveco', 'Isuzu', 'Jaguar',
                           'Jeep', 'JCB', 'Kamaz', 'KIA', 'Land Rover', 'Lada', 'Lexus', 'Mazda',
                           'MAN', 'Mercedes-Benz', 'Mitsubishi', 'Nissan', 'Opel', 'Peugeot',
                           'Renault', 'Skoda', 'Scania', 'SsangYong', 'Subaru', 'Suzuki',
                           'Toyota', 'Tofas', 'Tesla', 'UAZ', 'Volkswagen', 'Volvo', 'WAZ', 'GAZ',
                           'Yamaha', 'Zil', 'Other')
    brand_type = StatusField(choices_name='brand_choice')
    sell_choice = Choices('Sell', 'Rent')
    sell_type = StatusField(choices_name='sell_choice')
    year_choice = Choices('1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991',
                       '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003',
                       '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015',
                       '2017', '2018', '2019', '2020', '2021', '2022')
    year_type = StatusField(choices_name='year_choice')
    color = models.CharField(max_length=55)
    credit = models.BooleanField(default=False)
    change = models.BooleanField(default=False)
    mile = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999)], null=True, blank=True)
    engine_type_choice = Choices('Petrol', 'Diesel')
    engine_type = StatusField(choices_name='engine_type_choice')
    transmission_choice = Choices('automatic', 'manual')
    transmission_type = StatusField(choices_name='transmission_choice')
    motor_v_choice = Choices('0.5', '0.6', '0.7', '0.8', '0.9', '1', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7',
                             '1.8', '1.9', '2', '2.1', '2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '2.9', '3', '3.1',
                             '3.2', '3.3', '3.4', '3.5', '3.6', '3.7', '3.8', '3.9', '4', '4.1', '4.2', '4.3', '4.4', '4.5',
                             '4.6', '4.7', '4.8', '4.9', '5', '5.3', '5.5', '6')
    motor_v_type = StatusField(choices_name='motor_v_choice')

    def __str__(self):
        return self.brand_type


class Car(Transport):

    body_choice = Choices('Sedan', 'Coupe', 'Hatchback', 'Cabriolet', 'Universal', 'SUV',
                          'Grand Tourer', 'Crossover', 'Van', 'Pickup', 'Minivan', 'Minibus', 'Bus')
    body_type = StatusField(choices_name='body_choice')
    wheel_choice = Choices('Left', 'Right')
    wheel_type = StatusField(choices_name='wheel_choice')
    drive_unit_choice = Choices('Front', 'Rear', '4x4')
    drive_unit_type = StatusField(choices_name='drive_unit_choice')

    def __str__(self):
        return self.body_type


class CarImage(models.Model):

    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='car_images')
    images = models.ImageField(upload_to='transport/car_images/', null=True, blank=True)


class Motorcycle(Transport):

    motor_engin_choice = Choices('Inline Engines', 'Single Cylinder', 'Parallel Twin', 'Inline Triple&Four',
                    'V-Engines', 'V-Twin', 'V-Four', 'Flat Engines', 'Flat 4', 'Other')
    motor_engin_type = StatusField(choices_name='motor_engin_choice')

    def __str__(self):
        return self.motor_engin_type


class MotorcycleImage(models.Model):

    motorcycle = models.ForeignKey(Motorcycle, on_delete=models.CASCADE, related_name='motorcycle_images')
    images = models.ImageField(upload_to='transport/motorcycle_images/', null=True, blank=True)


class Truck(Transport):

    truck_choice = Choices('Tractor', 'Tow Truck', 'Fire Engine', 'Cement Mixer', 'Tanker',
                           'Trailer', 'Car Transport', 'Forklift', 'Excavator', 'Crane',
                           'Road Roller', 'Dump Truck', 'Bulldozer', 'Other')
    truck_type = StatusField(choices_name='truck_choice')

    def __str__(self):
        return self.truck_type


class TruckImage(models.Model):

    truck = models.ForeignKey(Truck, on_delete=models.CASCADE, related_name='motorcycle_images')
    images = models.ImageField(upload_to='transport/truck_images/', null=True, blank=True)
