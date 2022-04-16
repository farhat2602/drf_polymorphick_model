from PIL import Image
from django.contrib.auth import get_user_model
from django.db import models
from model_utils import Choices
from model_utils.fields import StatusField

from post.models import Post

User = get_user_model()


class Job(Post):

    activity_field_choice = Choices('Advocacy&LegalAdvice','Finance&Banking', 'Education', 'IT&Software',
                                    'Design&Creativity', 'Business&StrategicManagement', 'Sales',
                                    'Merchandising&Retailing', 'Marketing&Product Management', 'Health',
                                    'Beauty&Care', 'Entertainment&Activities', 'Logistics&Transport',
                                    'Restaurant&Accommodation', 'Textile', 'Agriculture&Livestock',
                                    'Protection and Security', 'PartTime&AdditionalJobs')
    activity_field_type = StatusField(choices_name='activity_field_choice')
    experience = models.CharField(max_length=100)

    def __str__(self):
        return self.activity_field_type


class Vacancy(Job):

    company_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.company_name


class VacancyImage(models.Model):

    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='vacancy_images')
    images = models.ImageField(upload_to='job/vacancy_images/', null=True, blank=True)


class Resume(Job):

    profession = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.profession


class ResumeImage(models.Model):

    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='resume_images')
    images = models.ImageField(upload_to='job/resume_images/', null=True, blank=True)
