# Generated by Django 3.0.3 on 2020-03-05 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0015_merge_20200301_1239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='avg_rating',
        ),
    ]
