# Generated by Django 2.2.12 on 2021-01-13 12:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pixx', '0004_auto_20210102_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactformmodel',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
