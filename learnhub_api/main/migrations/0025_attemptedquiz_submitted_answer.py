# Generated by Django 5.0.4 on 2024-05-11 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_attemptedquiz'),
    ]

    operations = [
        migrations.AddField(
            model_name='attemptedquiz',
            name='submitted_answer',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
