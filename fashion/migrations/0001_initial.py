# Generated by Django 4.0.3 on 2022-04-12 13:50

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
            name='Accessories',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='post.post')),
                ('gender_type', model_utils.fields.StatusField(choices=[('Unisex', 'Unisex'), ('Man', 'Man'), ('Woman', 'Woman'), ('Child', 'Child')], default='Unisex', max_length=100, no_check_for_status=True)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('post.post',),
        ),
        migrations.CreateModel(
            name='Bag',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='post.post')),
                ('gender_type', model_utils.fields.StatusField(choices=[('Unisex', 'Unisex'), ('Man', 'Man'), ('Woman', 'Woman'), ('Child', 'Child')], default='Unisex', max_length=100, no_check_for_status=True)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('post.post',),
        ),
        migrations.CreateModel(
            name='ChildClothes',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='post.post')),
                ('clothes_type', model_utils.fields.StatusField(choices=[('Tshirt', 'Tshirt'), ('Shirt', 'Shirt'), ('Skirt', 'Skirt'), ('Blouse', 'Blouse'), ('Dress', 'Dress'), ('SweatShirt', 'SweatShirt'), ('Classic Suit', 'Classic Suit'), ('Jacket', 'Jacket'), ('Shorts', 'Shorts'), ('Pant', 'Pant'), ('Jeans', 'Jeans'), ('JeansJacket', 'JeansJacket'), ('Coat', 'Coat'), ('SportWear', 'SportWear')], default='Tshirt', max_length=100, no_check_for_status=True)),
                ('size_type', model_utils.fields.StatusField(choices=[('1-3 month', '1-3 month'), ('3-5 month', '3-5 month'), ('5-7 month', '5-7 month'), ('8-10 month', '8-10 month'), ('1 year', '1 year'), ('2-3 year', '2-3 year'), ('4-5 year', '4-5 year'), ('6-7 year', '6-7 year'), ('8-10 year', '8-10 year')], default='1-3 month', max_length=100, no_check_for_status=True)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('post.post',),
        ),
        migrations.CreateModel(
            name='Cosmetic',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='post.post')),
                ('gender_type', model_utils.fields.StatusField(choices=[('Unisex', 'Unisex'), ('Man', 'Man'), ('Woman', 'Woman'), ('Child', 'Child')], default='Unisex', max_length=100, no_check_for_status=True)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('post.post',),
        ),
        migrations.CreateModel(
            name='ManClothes',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='post.post')),
                ('clothes_type', model_utils.fields.StatusField(choices=[('Tshirt', 'Tshirt'), ('Shirt', 'Shirt'), ('SweatShirt', 'SweatShirt'), ('Classic Suit', 'Classic Suit'), ('Jacket', 'Jacket'), ('Shorts', 'Shorts'), ('Pant', 'Pant'), ('Jeans', 'Jeans'), ('JeansJacket', 'JeansJacket'), ('Coat', 'Coat'), ('SportWear', 'SportWear')], default='Tshirt', max_length=100, no_check_for_status=True)),
                ('size_type', model_utils.fields.StatusField(choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL'), ('3XL', '3XL'), ('4XL', '4XL'), ('5XL', '5XL')], default='XS', max_length=100, no_check_for_status=True)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('post.post',),
        ),
        migrations.CreateModel(
            name='Shoes',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='post.post')),
                ('gender_type', model_utils.fields.StatusField(choices=[('Man', 'Man'), ('Woman', 'Woman'), ('Child', 'Child')], default='Man', max_length=100, no_check_for_status=True)),
                ('shoes_type', model_utils.fields.StatusField(choices=[('Daily', 'Daily'), ('Sport', 'Sport'), ('Classic', 'Classic'), ('Sandals', 'Sandals'), ('Outdoor', 'Outdoor')], default='Daily', max_length=100, no_check_for_status=True)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('post.post',),
        ),
        migrations.CreateModel(
            name='Textile',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='post.post')),
                ('type', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('post.post',),
        ),
        migrations.CreateModel(
            name='Underwear',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='post.post')),
                ('gender_type', model_utils.fields.StatusField(choices=[('Man', 'Man'), ('Woman', 'Woman'), ('Child', 'Child')], default='Man', max_length=100, no_check_for_status=True)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('post.post',),
        ),
        migrations.CreateModel(
            name='Watch',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='post.post')),
                ('gender_type', model_utils.fields.StatusField(choices=[('Unisex', 'Unisex'), ('Man', 'Man'), ('Woman', 'Woman'), ('Child', 'Child')], default='Unisex', max_length=100, no_check_for_status=True)),
                ('watch_type', model_utils.fields.StatusField(choices=[('Smart', 'Smart'), ('Mechanic', 'Mechanic')], default='Smart', max_length=100, no_check_for_status=True)),
                ('state_type', model_utils.fields.StatusField(choices=[('New', 'New'), ('2Hand', '2Hand')], default='New', max_length=100, no_check_for_status=True)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('post.post',),
        ),
        migrations.CreateModel(
            name='WomanClothes',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='post.post')),
                ('clothes_type', model_utils.fields.StatusField(choices=[('Tshirt', 'Tshirt'), ('Shirt', 'Shirt'), ('Skirt', 'Skirt'), ('Blouse', 'Blouse'), ('Dress', 'Dress'), ('SweatShirt', 'SweatShirt'), ('Classic Suit', 'Classic Suit'), ('Jacket', 'Jacket'), ('Shorts', 'Shorts'), ('Pant', 'Pant'), ('Jeans', 'Jeans'), ('JeansJacket', 'JeansJacket'), ('Coat', 'Coat'), ('SportWear', 'SportWear')], default='Tshirt', max_length=100, no_check_for_status=True)),
                ('size_type', model_utils.fields.StatusField(choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL'), ('3XL', '3XL'), ('4XL', '4XL'), ('5XL', '5XL')], default='XS', max_length=100, no_check_for_status=True)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('post.post',),
        ),
        migrations.CreateModel(
            name='WomanClothesImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='fashion/woman_clothes_images/')),
                ('woman_clothes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='fashion.womanclothes')),
            ],
        ),
        migrations.CreateModel(
            name='WatchImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='fashion/watch_images/')),
                ('watch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='fashion.watch')),
            ],
        ),
        migrations.CreateModel(
            name='UnderwearImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='fashion/underwear_images/')),
                ('underwear', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='fashion.underwear')),
            ],
        ),
        migrations.CreateModel(
            name='TextileImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='fashion/textile_images/')),
                ('accessories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='fashion.textile')),
            ],
        ),
        migrations.CreateModel(
            name='ShoesImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='fashion/shoes_images/')),
                ('shoes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='fashion.shoes')),
            ],
        ),
        migrations.CreateModel(
            name='ManClothesImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='fashion/man_clothes_images/')),
                ('man_clothes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='fashion.manclothes')),
            ],
        ),
        migrations.CreateModel(
            name='CosmeticImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='fashion/cosmetic_images/')),
                ('cosmetic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='fashion.cosmetic')),
            ],
        ),
        migrations.CreateModel(
            name='ChildClothesImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='fashion/child_clothes_images/')),
                ('child_clothes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='fashion.childclothes')),
            ],
        ),
        migrations.CreateModel(
            name='BagImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='fashion/bag_images/')),
                ('bag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='fashion.bag')),
            ],
        ),
        migrations.CreateModel(
            name='AccessoriesImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='fashion/accessories_images/')),
                ('accessories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='fashion.accessories')),
            ],
        ),
    ]
