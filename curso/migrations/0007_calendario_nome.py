# Generated by Django 3.2.5 on 2021-07-05 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0006_calendario_foto2'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendario',
            name='nome',
            field=models.CharField(default='calendario', max_length=20),
        ),
    ]
