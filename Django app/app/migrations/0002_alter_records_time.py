# Generated by Django 4.0.1 on 2022-08-27 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='records',
            name='Time',
            field=models.DecimalField(decimal_places=5, max_digits=20),
        ),
    ]
