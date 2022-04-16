# Generated by Django 4.0.3 on 2022-04-12 13:50

from django.db import migrations, models
import django.db.models.deletion
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('post', '0001_initial'),
        ('electronic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Electronic',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='post.post')),
                ('state_type', model_utils.fields.StatusField(choices=[('New', 'New'), ('2Hand', '2Hand')], default='New', max_length=100, no_check_for_status=True)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('post.post',),
        ),
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('electronic_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='electronic.electronic')),
                ('brand_type', model_utils.fields.StatusField(choices=[('Fujifilm', 'Fujifilm'), ('Canon', 'Canon'), ('Xiaomi', 'Xiaomi'), ('Sony', 'Sony'), ('Kodak', 'Kodak'), ('Heider', 'Heider'), ('Nikon', 'Nikon'), ('Dijimedia', 'Dijimedia'), ('BLUE İNTER', 'BLUE İNTER'), ('EKEN', 'EKEN'), ('Samsung', 'Samsung'), ('Skygo', 'Skygo'), ('DJI', 'DJI'), ('Everest', 'Everest'), ('OEM', 'OEM'), ('Retro', 'Retro'), ('Zore', 'Zore'), ('Panasonic', 'Panasonic'), ('Baseus', 'Baseus'), ('KAISER', 'KAISER'), ('Enshall', 'Enshall'), ('Sandisk', 'Sandisk'), ('Dahua', 'Dahua'), ('Olympus', 'Olympus'), ('Platoon', 'Platoon'), ('Benks', 'Benks'), ('Polaroid', 'Polaroid'), ('Chermik', 'Chermik'), ('Tucano', 'Tucano'), ('Duracell', 'Duracell'), ('Addison', 'Addison'), ('logitech', 'logitech'), ('HP', 'HP'), ('Vision', 'Vision'), ('Zoom', 'Zoom'), ('Beta', 'Beta'), ('Oppo', 'Oppo'), ('Apple', 'Apple'), ('Kingston', 'Kingston'), ('KAYAMU', 'KAYAMU'), ('LG', 'LG'), ('Toshiba', 'Toshiba'), ('NEVO', 'NEVO'), ('other', 'other')], default='Fujifilm', max_length=100, no_check_for_status=True)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('electronic.electronic',),
        ),
        migrations.CreateModel(
            name='Desktop',
            fields=[
                ('electronic_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='electronic.electronic')),
                ('brand_type', model_utils.fields.StatusField(choices=[('Apple', 'Apple'), ('Acer', 'Acer'), ('Asus', 'Asus'), ('Beko', 'Beko'), ('Casper', 'Casper'), ('Dell', 'Dell'), ('HP', 'HP'), ('Lenovo', 'Lenovo'), ('LG', 'LG'), ('Microsoft', 'Microsoft'), ('Msi', 'Msi'), ('Monster', 'Monster'), ('Samsung', 'Samsung'), ('Toshiba', 'Toshiba'), ('Xiaomi', 'Xiaomi'), ('Other', 'Other')], default='Apple', max_length=100, no_check_for_status=True)),
                ('ram_memory_type', model_utils.fields.StatusField(choices=[('1Gb', '1Gb'), ('2Gb', '2Gb'), ('3Gb', '3Gb'), ('4Gb', '4Gb'), ('6Gb', '6Gb'), ('8Gb', '8Gb'), ('16GB', '16GB'), ('32GB', '32GB'), ('64GB', '64GB')], default='1Gb', max_length=100, no_check_for_status=True)),
                ('memory_type', model_utils.fields.StatusField(choices=[('16Gb', '16Gb'), ('32Gb', '32Gb'), ('64Gb', '64Gb'), ('128Gb', '128Gb'), ('256Gb', '256Gb'), ('512Gb', '512Gb'), ('1TB', '1TB'), ('2TB', '2TB'), ('4TB', '4TB')], default='16Gb', max_length=100, no_check_for_status=True)),
                ('disk_type', model_utils.fields.StatusField(choices=[('SSD', 'SSD'), ('HDD', 'HDD')], default='SSD', max_length=100, no_check_for_status=True)),
                ('guaranty', models.CharField(blank=True, max_length=124, null=True)),
                ('change', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('electronic.electronic',),
        ),
        migrations.CreateModel(
            name='GameConsole',
            fields=[
                ('electronic_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='electronic.electronic')),
                ('game_type', model_utils.fields.StatusField(choices=[('Playstation', 'Playstation'), ('Xbox', 'Xbox')], default='Playstation', max_length=100, no_check_for_status=True)),
                ('brand_type', model_utils.fields.StatusField(choices=[('Sony', 'Sony'), ('GoldMaster', 'GoldMaster'), ('gamam', 'gamam'), ('2K Games', '2K Games'), ('Ubisoft', 'Ubisoft'), ('logitech', 'logitech'), ('RockStar Games', 'RockStar Games'), ('Polygold', 'Polygold')], default='Sony', max_length=100, no_check_for_status=True)),
                ('memory_type', model_utils.fields.StatusField(choices=[('160 GB', '160 GB'), ('320 GB', '320 GB'), ('500 GB', '500 GB'), ('825 GB', '825 GB'), ('1 TB', '1 TB'), ('2 TB', '2 TB')], default='160 GB', max_length=100, no_check_for_status=True)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('electronic.electronic',),
        ),
        migrations.CreateModel(
            name='Headphone',
            fields=[
                ('electronic_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='electronic.electronic')),
                ('type', model_utils.fields.StatusField(choices=[('Bluetooth', 'Bluetooth'), ('3.5mm', '3.5mm')], default='Bluetooth', max_length=100, no_check_for_status=True)),
                ('brand', models.CharField(max_length=24)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('electronic.electronic',),
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('electronic_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='electronic.electronic')),
                ('brand_type', model_utils.fields.StatusField(choices=[('Apple', 'Apple'), ('Acer', 'Acer'), ('Asus', 'Asus'), ('BlackBerry', 'BlackBerry'), ('Casper', 'Casper'), ('Dell', 'Dell'), ('Google', 'Google'), ('Huawei', 'Huawei'), ('Honor', 'Honor'), ('HomeTech', 'HomeTech'), ('HP', 'HP'), ('Lenovo', 'Lenovo'), ('LG', 'LG'), ('Microsoft', 'Microsoft'), ('Msi', 'Msi'), ('Monster', 'Monster'), ('Redmi', 'Redmi'), ('Samsung', 'Samsung'), ('Sony', 'Sony'), ('Toshiba', 'Toshiba'), ('Xiaomi', 'Xiaomi'), ('Other', 'Other')], default='Apple', max_length=100, no_check_for_status=True)),
                ('screen_diagonal_type', model_utils.fields.StatusField(choices=[('10', '10'), ('13', '13'), ('13.3', '13.3'), ('14', '14'), ('15', '15'), ('15.6', '15.6'), ('16', '16'), ('16.1', '16.1'), ('17.3', '17.3')], default='10', max_length=100, no_check_for_status=True)),
                ('discrete_video_card', models.BooleanField(default=False)),
                ('graphic_card_type', model_utils.fields.StatusField(choices=[('1Gb', '1Gb'), ('2Gb', '2Gb'), ('3Gb', '3Gb'), ('4Gb', '4Gb'), ('6Gb', '6Gb'), ('8Gb', '8Gb'), ('16GB', '16GB'), ('32GB', '32GB')], default='1Gb', max_length=100, no_check_for_status=True)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('electronic.electronic',),
        ),
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('electronic_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='electronic.electronic')),
                ('brand_type', model_utils.fields.StatusField(choices=[('ASUS', 'ASUS'), ('LENOVO', 'LENOVO'), ('HP', 'HP'), ('ACER', 'ACER'), ('Huawei', 'Huawei'), ('Monster', 'Monster'), ('Casper', 'Casper'), ('DELL', 'DELL'), ('MSI', 'MSI'), ('FUJITSU', 'FUJITSU'), ('Microsoft', 'Microsoft'), ('TOSHIBA', 'TOSHIBA'), ('Honor', 'Honor'), ('RAZER', 'RAZER'), ('VESTEL', 'VESTEL'), ('Intel', 'Intel'), ('Samsung', 'Samsung'), ('other', 'other')], default='ASUS', max_length=100, no_check_for_status=True)),
                ('wfi', models.BooleanField(default=False)),
                ('hdmi', models.BooleanField(default=False)),
                ('vga', models.BooleanField(default=False)),
                ('screen_diagonal_type', model_utils.fields.StatusField(choices=[('7', '7'), ('10', '10'), ('14', '14'), ('15', '15'), ('15.6', '15.6'), ('17', '17'), ('18.5', '18.5'), ('19', '19'), ('19.5', '19.5'), ('20', '20'), ('20.7', '20.7'), ('21', '21'), ('22', '22'), ('23', '23'), ('23.5', '23.5'), ('24', '24'), ('25', '25'), ('27', '27'), ('28', '28'), ('29', '29'), ('31', '31'), ('32', '32'), ('34', '34'), ('35', '35'), ('4955', '4955')], default='7', max_length=100, no_check_for_status=True)),
                ('hz_type', model_utils.fields.StatusField(choices=[('60', '60'), ('72', '72'), ('75', '75'), ('83', '83'), ('100', '100'), ('120', '120'), ('144', '144'), ('165', '165'), ('200', '200'), ('240', '240')], default='60', max_length=100, no_check_for_status=True)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('electronic.electronic',),
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('electronic_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='electronic.electronic')),
                ('phone_type', model_utils.fields.StatusField(choices=[('Smartphone', 'Smartphone'), ('DialPhone', 'DialPhone')], default='Smartphone', max_length=100, no_check_for_status=True)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('electronic.electronic',),
        ),
        migrations.CreateModel(
            name='Printer',
            fields=[
                ('electronic_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='electronic.electronic')),
                ('printer_type', model_utils.fields.StatusField(choices=[('Printer', 'Printer'), ('Copy', 'Copy'), ('Scanner', 'Scanner')], default='Printer', max_length=100, no_check_for_status=True)),
                ('brand', models.CharField(max_length=55)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('electronic.electronic',),
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('electronic_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='electronic.electronic')),
                ('brand_type', model_utils.fields.StatusField(choices=[('Polygold', 'Polygold'), ('JBL', 'JBL'), ('Xiaomi', 'Xiaomi'), ('Pioneer', 'Pioneer'), ('logitech', 'logitech'), ('Snopy', 'Snopy'), ('Harman Kardon', 'Harman Kardon'), ('Sony', 'Sony'), ('Piranha', 'Piranha'), ('Sunix', 'Sunix'), ('Torima', 'Torima'), ('LG', 'LG'), ('Samsung', 'Samsung'), ('Mikado', 'Mikado'), ('HP', 'HP'), ('Philips', 'Philips'), ('LENOVO', 'LENOVO'), ('Havana', 'Havana'), ('other', 'other')], default='Polygold', max_length=100, no_check_for_status=True)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('electronic.electronic',),
        ),
        migrations.CreateModel(
            name='Tablet',
            fields=[
                ('electronic_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='electronic.electronic')),
                ('brand_type', model_utils.fields.StatusField(choices=[('Apple', 'Apple'), ('Asus', 'Asus'), ('Beko', 'Beko'), ('Google', 'Google'), ('Huawei', 'Huawei'), ('Honor', 'Honor'), ('Lenovo', 'Lenovo'), ('LG', 'LG'), ('Microsoft', 'Microsoft'), ('Motorola', 'Motorola'), ('Nokia', 'Nokia'), ('Oppo', 'Oppo'), ('Redmi', 'Redmi'), ('Samsung', 'Samsung'), ('Sony', 'Sony'), ('Xiaomi', 'Xiaomi'), ('ZTE', 'ZTE'), ('Other', 'Other')], default='Apple', max_length=100, no_check_for_status=True)),
                ('memory_type', model_utils.fields.StatusField(choices=[('16Gb', '16Gb'), ('32Gb', '32Gb'), ('64Gb', '64Gb'), ('128Gb', '128Gb'), ('256Gb', '256Gb'), ('512Gb', '512Gb'), ('1TB', '1TB')], default='16Gb', max_length=100, no_check_for_status=True)),
                ('ram_memory_type', model_utils.fields.StatusField(choices=[('1Gb', '1Gb'), ('2Gb', '2Gb'), ('3Gb', '3Gb'), ('4Gb', '4Gb'), ('6Gb', '6Gb'), ('8Gb', '8Gb'), ('16GB', '16GB'), ('32GB', '32GB')], default='1Gb', max_length=100, no_check_for_status=True)),
                ('sim', models.BooleanField(default=False)),
                ('network', model_utils.fields.StatusField(choices=[('2G', '2G'), ('3G', '3G'), ('4G', '4G'), ('4.5G', '4.5G'), ('5G', '5G')], default='2G', max_length=100, no_check_for_status=True)),
                ('nfc', models.BooleanField(default=False)),
                ('face_id', models.BooleanField(default=False)),
                ('guaranty', models.CharField(blank=True, max_length=124, null=True)),
                ('change', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('electronic.electronic',),
        ),
        migrations.CreateModel(
            name='DialPhone',
            fields=[
                ('phone_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='electronic.phone')),
                ('brand_type', model_utils.fields.StatusField(choices=[('Samsung', 'Samsung'), ('Nokia', 'Nokia'), ('LG', 'LG'), ('BlackBerry', 'BlackBerry'), ('TCL', 'TCL'), ('VESTEL', 'VESTEL'), ('LENOVO', 'LENOVO'), ('Alcatel', 'Alcatel'), ('Motorola', 'Motorola'), ('Panasonic', 'Panasonic'), ('other', 'other')], default='Samsung', max_length=100, no_check_for_status=True)),
                ('have_camera', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('electronic.phone',),
        ),
        migrations.CreateModel(
            name='Smartphone',
            fields=[
                ('phone_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='electronic.phone')),
                ('brand_type', model_utils.fields.StatusField(choices=[('Samsung', 'Samsung'), ('Apple', 'Apple'), ('Xiaomi', 'Xiaomi'), ('Nokia', 'Nokia'), ('Reeder', 'Reeder'), ('General Mobile', 'General Mobile'), ('Oppo', 'Oppo'), ('Realme', 'Realme'), ('LG', 'LG'), ('Huawei', 'Huawei'), ('BlackBerry', 'BlackBerry'), ('POCO', 'POCO'), ('Casper', 'Casper'), ('TCL', 'TCL'), ('VESTEL', 'VESTEL'), ('LENOVO', 'LENOVO'), ('Alcatel', 'Alcatel'), ('Htc', 'Htc'), ('ZTE', 'ZTE'), ('Motorola', 'Motorola'), ('OnePlus', 'OnePlus'), ('Meizu', 'Meizu'), ('Honor', 'Honor'), ('Panasonic', 'Panasonic'), ('Turkcell', 'Turkcell'), ('Turk Telekom', 'Turk Telekom'), ('Syrox', 'Syrox'), ('Asus', 'Asus')], default='Samsung', max_length=100, no_check_for_status=True)),
                ('memory_type', model_utils.fields.StatusField(choices=[('8GB', '8GB'), ('16GB', '16GB'), ('32GB', '32GB'), ('64GB', '64GB'), ('128GB', '128GB'), ('256GB', '256GB'), ('512GB', '512GB'), ('1TB', '1TB')], default='8GB', max_length=100, no_check_for_status=True)),
                ('ram_memory_type', model_utils.fields.StatusField(choices=[('1GB', '1GB'), ('2GB', '2GB'), ('3GB', '3GB'), ('4GB', '4GB'), ('6GB', '6GB'), ('8GB', '8GB'), ('16GB', '16GB'), ('32GB', '32GB')], default='1GB', max_length=100, no_check_for_status=True)),
                ('dual_sim', models.BooleanField(default=False)),
                ('nfc', models.BooleanField(default=False)),
                ('face_id', models.BooleanField(default=False)),
                ('network', model_utils.fields.StatusField(choices=[('2G', '2G'), ('3G', '3G'), ('4G', '4G'), ('4.5G', '4.5G'), ('5G', '5G')], default='2G', max_length=100, no_check_for_status=True)),
                ('guaranty', models.CharField(blank=True, max_length=124, null=True)),
                ('change', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('electronic.phone',),
        ),
        migrations.CreateModel(
            name='TabletImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, null=True, upload_to='electronic/tablet_images/')),
                ('tablet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tablet_images', to='electronic.tablet')),
            ],
        ),
        migrations.CreateModel(
            name='SpeakerImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='electronic/speaker_images/')),
                ('speaker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='speaker_images', to='electronic.speaker')),
            ],
        ),
        migrations.CreateModel(
            name='PrinterImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='electronic/printer_images/')),
                ('printer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='printer_images', to='electronic.printer')),
            ],
        ),
        migrations.CreateModel(
            name='MonitorImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, null=True, upload_to='electronic/monitor_images/')),
                ('monitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='monitor_images', to='electronic.monitor')),
            ],
        ),
        migrations.CreateModel(
            name='LaptopImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, null=True, upload_to='electronic/laptop_images/')),
                ('laptop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='laptop_images', to='electronic.laptop')),
            ],
        ),
        migrations.CreateModel(
            name='HeadphoneImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='electronic/headphone_images/')),
                ('headphone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='headphone_images', to='electronic.headphone')),
            ],
        ),
        migrations.CreateModel(
            name='GameConsoleImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='electronic/game_console_images/')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game_console_images', to='electronic.gameconsole')),
            ],
        ),
        migrations.AddField(
            model_name='desktopimage',
            name='desktop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='desktop_images', to='electronic.desktop'),
        ),
        migrations.AddField(
            model_name='cameraimage',
            name='camera',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='camera_images', to='electronic.camera'),
        ),
        migrations.CreateModel(
            name='SmartphoneImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, null=True, upload_to='electronic/smartphone_images/')),
                ('smartphone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='smartphone_images', to='electronic.smartphone')),
            ],
        ),
        migrations.AddField(
            model_name='dialphoneimage',
            name='dial_phone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dial_phone_images', to='electronic.dialphone'),
        ),
    ]
