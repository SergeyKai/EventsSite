# Generated by Django 5.0.2 on 2024-04-12 08:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='events', to=settings.AUTH_USER_MODEL),
        ),
    ]
