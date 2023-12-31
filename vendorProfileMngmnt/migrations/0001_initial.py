# Generated by Django 4.2.7 on 2023-12-03 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('name', models.CharField(max_length=20)),
                ('contact_details', models.TextField(max_length=30)),
                ('address', models.TextField(max_length=100)),
                ('vendor_code', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('on_time_delivery_rate', models.FloatField(max_length=20)),
                ('quality_rating_avg', models.FloatField(max_length=20)),
                ('average_response_time', models.FloatField(max_length=20)),
                ('fulfillment_rate', models.FloatField(max_length=20)),
            ],
        ),
    ]
