# Generated by Django 3.1.3 on 2020-11-11 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0004_auto_20201110_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='master',
            name='certification',
            field=models.ManyToManyField(null=True, to='room.Certificate'),
        ),
    ]