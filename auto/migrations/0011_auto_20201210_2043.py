# Generated by Django 3.1.2 on 2020-12-10 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0010_auto_20201210_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='velocidad_maxima',
            field=models.CharField(max_length=6),
        ),
    ]