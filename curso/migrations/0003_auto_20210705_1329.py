# Generated by Django 3.2.5 on 2021-07-05 12:29

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0002_auto_20210705_1308'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Agenda',
            new_name='AgendaTeste',
        ),
        migrations.CreateModel(
            name='Entrega',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='curso.disciplina')),
                ('sala', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='curso.sala')),
            ],
        ),
    ]
