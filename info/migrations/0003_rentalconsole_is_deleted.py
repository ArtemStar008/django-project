# Generated by Django 4.2.6 on 2023-10-30 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_rentalconsole'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentalconsole',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]