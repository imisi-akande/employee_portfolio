# Generated by Django 2.1.2 on 2018-11-15 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_auto_20181115_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='description',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
