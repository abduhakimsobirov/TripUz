# Generated by Django 3.2.4 on 2021-06-15 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0004_alter_trip_driver'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='address',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
