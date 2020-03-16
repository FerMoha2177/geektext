# Generated by Django 3.0.2 on 2020-02-03 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0009_auto_20200203_1816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='price',
        ),
        migrations.AddField(
            model_name='book',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]
