# Generated by Django 3.2.7 on 2021-09-20 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telemedicine', '0005_alter_patients_smoking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='smoking',
            field=models.BooleanField(default=False),
        ),
    ]
