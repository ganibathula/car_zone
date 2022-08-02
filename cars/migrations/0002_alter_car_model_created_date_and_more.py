# Generated by Django 4.0.5 on 2022-07-17 06:47

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car_model',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 17, 12, 17, 3, 749800)),
        ),
        migrations.AlterField(
            model_name='car_model',
            name='description',
            field=ckeditor.fields.RichTextField(max_length=400),
        ),
    ]
