# Generated by Django 5.0.7 on 2024-08-12 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_rename_psot_comment_post'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-create_date']},
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
