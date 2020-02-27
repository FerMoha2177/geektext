# Generated by Django 2.1.5 on 2020-02-14 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0012_auto_20200204_2358'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='ISBN',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='dimensions',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='synopsis',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
