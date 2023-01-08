# Generated by Django 4.1.5 on 2023-01-08 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_person_report'),
    ]

    operations = [
        migrations.CreateModel(
            name='wanted_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reported_by_name', models.CharField(blank=True, max_length=100, null=True)),
                ('reported_by_phone', models.CharField(blank=True, max_length=100, null=True)),
                ('reported_by_address', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('hair_description', models.CharField(max_length=100)),
                ('height_description', models.CharField(max_length=100)),
                ('cloth_description', models.CharField(max_length=100)),
                ('caught_crime', models.CharField(max_length=100)),
                ('caught_location', models.CharField(blank=True, max_length=100, null=True)),
                ('caught_date', models.DateField()),
                ('caught_time', models.TimeField()),
                ('save_date_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
