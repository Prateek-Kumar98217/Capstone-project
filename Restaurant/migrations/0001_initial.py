# Generated by Django 5.1.6 on 2025-02-25 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('ID', models.IntegerField(max_length=11, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255)),
                ('No_of_guests', models.IntegerField(max_length=6)),
                ('BookingDate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('ID', models.IntegerField(max_length=5, primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=255)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Inventory', models.IntegerField(max_length=5)),
            ],
        ),
    ]
