# Generated by Django 2.1.2 on 2018-11-15 00:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_auto_20181115_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='employer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departments', to=settings.AUTH_USER_MODEL),
        ),
    ]
