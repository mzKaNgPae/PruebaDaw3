# Generated by Django 3.1.2 on 2020-12-10 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0011_auto_20201210_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='velocidad_maxima',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
