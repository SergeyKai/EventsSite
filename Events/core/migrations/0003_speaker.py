# Generated by Django 5.0.2 on 2024-02-22 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_event_options_event_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Спикер',
                'verbose_name_plural': 'Спикеры',
            },
        ),
    ]