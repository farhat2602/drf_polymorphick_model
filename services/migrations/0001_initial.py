# Generated by Django 4.0.3 on 2022-04-13 09:12

from django.db import migrations, models
import django.db.models.deletion
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='post.post')),
                ('service_type', model_utils.fields.StatusField(choices=[('TransportLogistic', 'TransportLogistic'), ('RepairConstruction', 'RepairConstruction'), ('BeautyHealth', 'BeautyHealth'), ('GardenPlot', 'GardenPlot'), ('EquipmentRepair', 'EquipmentRepair'), ('Cleaning', 'Cleaning'), ('Business', 'Business'), ('WeddingHolidayEvents', 'WeddingHolidayEvents'), ('Teachers', 'Teachers'), ('ITInternetTelecom', 'ITInternetTelecom'), ('Food', 'Food'), ('BabySisters', 'BabySisters'), ('Security', 'Security'), ('Delivery', 'Delivery'), ('Other', 'Other')], default='TransportLogistic', max_length=100, no_check_for_status=True)),
                ('company_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('post.post',),
        ),
        migrations.CreateModel(
            name='ServiceImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, null=True, upload_to='service_images/')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='services.service')),
            ],
        ),
    ]
