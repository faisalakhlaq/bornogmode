# Generated by Django 2.1 on 2018-08-18 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=128)),
                ('last_name', models.CharField(blank=True, max_length=128)),
                ('title', models.CharField(blank=True, max_length=128)),
                ('street', models.CharField(blank=True, max_length=128)),
                ('street_2', models.CharField(blank=True, max_length=128)),
                ('city', models.CharField(blank=True, max_length=128)),
                ('postcode', models.CharField(blank=True, max_length=128)),
                ('country', models.CharField(blank=True, max_length=128)),
                ('phone', models.CharField(blank=True, max_length=128)),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
    ]
