# Generated by Django 3.2.9 on 2021-11-04 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0007_auto_20211104_1139'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Appearance',
            new_name='Appearance_Image',
        ),
        migrations.RenameModel(
            old_name='Interior',
            new_name='Interior_Image',
        ),
    ]
