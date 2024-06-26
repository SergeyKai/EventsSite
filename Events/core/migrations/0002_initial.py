# Generated by Django 5.0.2 on 2024-04-12 08:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='users',
            field=models.ManyToManyField(blank=True, null=True, related_name='events', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='core.location'),
        ),
        migrations.AddField(
            model_name='event',
            name='speakers',
            field=models.ManyToManyField(related_name='events', to='core.speaker'),
        ),
        migrations.AddField(
            model_name='event',
            name='topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='core.topic'),
        ),
    ]
