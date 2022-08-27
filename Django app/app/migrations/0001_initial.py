# Generated by Django 4.0.1 on 2022-08-27 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Records',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Unnamed_0', models.IntegerField()),
                ('_id', models.CharField(blank=True, max_length=1000, null=True, unique=True)),
                ('Function', models.CharField(blank=True, max_length=1000, null=True)),
                ('Time', models.DecimalField(decimal_places=5, max_digits=6)),
                ('Error', models.CharField(max_length=1000)),
                ('time_stamp', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]