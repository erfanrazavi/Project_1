# Generated by Django 5.0.7 on 2024-08-09 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_newsletter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
