from django.db import models
from model_utils import Choices
from model_utils.fields import StatusField

from post.models import Post


class Service(Post):

    service_choice = Choices('TransportLogistic', 'RepairConstruction', 'BeautyHealth', 'GardenPlot',
                             'EquipmentRepair', 'Cleaning', 'Business', 'WeddingHolidayEvents', 'Teachers',
                             'ITInternetTelecom','Food', 'BabySisters', 'Security', 'Delivery', 'Other')
    service_type = StatusField(choices_name='service_choice')
    company_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.service_type


class ServiceImage(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='images')
    images = models.ImageField(upload_to='service_images/', null=True, blank=True)
