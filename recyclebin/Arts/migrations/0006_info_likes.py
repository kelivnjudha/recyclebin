# Generated by Django 4.2.5 on 2023-10-08 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Arts', '0005_alter_upload_options_rename_imgae_info_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
