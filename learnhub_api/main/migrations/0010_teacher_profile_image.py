# Generated by Django 5.0.4 on 2024-05-09 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_courserating'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='profile_image',
            field=models.ImageField(null=True, upload_to='teachers_images'),
        ),
    ]
