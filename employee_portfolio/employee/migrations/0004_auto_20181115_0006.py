# Generated by Django 2.1.2 on 2018-11-15 00:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_auto_20181114_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='department',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='department',
            name='employer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emails', to=settings.AUTH_USER_MODEL),
        ),
    ]