# Generated by Django 4.2.5 on 2023-09-25 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Arts', '0003_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='Contact',
            field=models.CharField(default='N/A', max_length=225),
        ),
        migrations.AddField(
            model_name='info',
            name='Title',
            field=models.CharField(default='N/A', max_length=225),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='info',
            name='reason_of_rejection',
            field=models.TextField(blank=True),
        ),
    ]