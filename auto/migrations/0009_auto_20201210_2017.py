# Generated by Django 3.1.2 on 2020-12-10 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0008_auto_20201210_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='descripcion',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
