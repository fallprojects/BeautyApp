# Generated by Django 3.1.3 on 2020-11-11 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0007_service_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='master',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to=''),
        ),
    ]