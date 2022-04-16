from rest_framework import serializers
from job.models import Job, Vacancy, VacancyImage, Resume, ResumeImage


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


class VacancyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = VacancyImage
        fields = '__all__'


class VacancySerializer(serializers.ModelSerializer):
    images = VacancyImageSerializer(many=True, required=False)

    class Meta:
        model = Vacancy
        fields = '__all__'


class ResumeImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResumeImage
        fields = '__all__'


class ResumeSerializer(serializers.ModelSerializer):
    images = ResumeImageSerializer(many=True, required=False, write_only=True)

    class Meta:
        model = Resume
        fields = '__all__'
