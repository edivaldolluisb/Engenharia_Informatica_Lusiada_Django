# Generated by Django 3.2.5 on 2021-07-05 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0003_auto_20210705_1329'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Entrega',
            new_name='AgendaEntrega',
        ),
    ]