# Generated by Django 3.2.9 on 2021-11-04 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0008_auto_20211104_1412'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interior_Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interior_details', to='car.car')),
            ],
        ),
        migrations.CreateModel(
            name='Appearance_Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appearance_details', to='car.car')),
            ],
        ),
    ]
