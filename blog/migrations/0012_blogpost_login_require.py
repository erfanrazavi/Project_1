# Generated by Django 5.0.7 on 2024-08-13 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_comment_options_alter_comment_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='login_require',
            field=models.BooleanField(default=False),
        ),
    ]
