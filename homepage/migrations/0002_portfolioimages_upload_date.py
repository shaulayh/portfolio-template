# Generated by Django 4.0.4 on 2022-05-02 15:09

from django.db import migrations, models
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolioimages',
            name='upload_date',
            field=models.DateTimeField(default=django.utils.datetime_safe.datetime.now),
        ),
    ]