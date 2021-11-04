# Generated by Django 3.2.9 on 2021-11-04 03:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('in_stock', models.BooleanField(default=True)),
                ('price', models.IntegerField()),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='car-main-image/%Y/%m/%d')),
                ('manufactured_at', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Car_Model_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PositionCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='video/%Y/%m/%d')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.car')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='car-price-image/%Y/%m/%d')),
                ('min_price', models.IntegerField()),
                ('transmission_name', models.CharField(max_length=255)),
                ('wheel_drive_name', models.CharField(max_length=255)),
                ('fuel_type_name', models.CharField(max_length=255)),
                ('engine_type', models.CharField(max_length=255)),
                ('engine_displacement', models.CharField(max_length=255)),
                ('engine_power', models.IntegerField()),
                ('working_volume', models.IntegerField()),
                ('time_to_100_speed', models.CharField(max_length=255)),
                ('max_speed', models.IntegerField()),
                ('car', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='car.car')),
                ('position_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.positioncategory')),
            ],
        ),
        migrations.CreateModel(
            name='Interior',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='car-interior-image/%Y/%m/%d')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.car')),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image/%Y/%m/%d')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.car')),
            ],
        ),
        migrations.CreateModel(
            name='Colored_Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.car')),
                ('position_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.positioncategory')),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_ibi', models.IntegerField()),
                ('color_title', models.CharField(max_length=255)),
                ('color_code', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='color-image/%Y/%m/%d')),
                ('colored_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.colored_image')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='car_model_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.car_model_type'),
        ),
        migrations.CreateModel(
            name='Attribute_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.position')),
            ],
        ),
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=2550)),
                ('attribute_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.attribute_category')),
            ],
        ),
        migrations.CreateModel(
            name='Appearance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='car-appearance-image/%Y/%m/%d')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.car')),
            ],
        ),
    ]
