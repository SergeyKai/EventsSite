# Generated by Django 5.0.2 on 2024-02-20 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('event_date', models.DateTimeField()),
                ('create_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
