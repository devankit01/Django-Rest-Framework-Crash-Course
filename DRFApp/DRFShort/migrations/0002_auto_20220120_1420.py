# Generated by Django 3.0.14 on 2022-01-20 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DRFShort', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='author',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='course',
            name='duration',
            field=models.FloatField(),
        ),
    ]
