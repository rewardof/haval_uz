# Generated by Django 3.2.9 on 2021-11-04 03:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0003_alter_color_color_ibi'),
    ]

    operations = [
        migrations.AddField(
            model_name='attribute_category',
            name='car_position',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='position', to='car.position'),
            preserve_default=False,
        ),
    ]