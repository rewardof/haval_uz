# Generated by Django 3.2.9 on 2021-11-04 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0006_auto_20211104_0922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attribute_category',
            name='position',
        ),
        migrations.AlterField(
            model_name='appearance',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appearance_images', to='car.car'),
        ),
        migrations.AlterField(
            model_name='attribute',
            name='attribute_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attributes', to='car.attribute_category'),
        ),
        migrations.AlterField(
            model_name='attribute_category',
            name='car_position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attribute_category', to='car.position'),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_model_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='car.car_model_type'),
        ),
        migrations.AlterField(
            model_name='colored_image',
            name='car_position_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='colored_images', to='car.image_for_car_positioncategory'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='galleries', to='car.car'),
        ),
        migrations.AlterField(
            model_name='image_for_car_positioncategory',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_for_car_positioncategory', to='car.car'),
        ),
        migrations.AlterField(
            model_name='image_for_car_positioncategory',
            name='position_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images_for_positioncategory', to='car.positioncategory'),
        ),
        migrations.AlterField(
            model_name='interior',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interior_images', to='car.car'),
        ),
        migrations.AlterField(
            model_name='position',
            name='car',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='positions', to='car.car'),
        ),
        migrations.AlterField(
            model_name='video',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='car.car'),
        ),
    ]