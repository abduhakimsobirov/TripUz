# Generated by Django 3.2.3 on 2021-06-13 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='datatime',
            field=models.DateTimeField(null=True),
        ),
    ]
