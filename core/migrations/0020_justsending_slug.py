# Generated by Django 5.0.4 on 2024-04-24 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_remove_justsending_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='justsending',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
    ]
