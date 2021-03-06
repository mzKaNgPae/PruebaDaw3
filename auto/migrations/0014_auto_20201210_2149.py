# Generated by Django 3.1.2 on 2020-12-11 00:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0013_auto_20201210_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='marca',
            name='pais',
            field=models.PositiveSmallIntegerField(choices=[(0, 'No definido'), (1, 'Alemania'), (2, 'Italia'), (3, 'Reino Unido'), (4, 'Estados Unidos'), (5, 'Japon'), (6, 'Francia')], default=0),
        ),
        migrations.CreateModel(
            name='Competencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=70)),
                ('anno', models.IntegerField(blank=True, max_length=4)),
                ('marca_campion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auto.marca')),
            ],
        ),
    ]
