# Generated by Django 4.1.7 on 2023-02-21 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_remove_restaurant_delivery_hours'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='location',
            field=models.CharField(max_length=255, null=True),
        ),
    ]