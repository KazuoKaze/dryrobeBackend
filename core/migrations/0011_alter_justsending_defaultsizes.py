# Generated by Django 5.0.4 on 2024-04-22 07:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_remove_justsending_defaultsizes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='justsending',
            name='defaultSizes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='defaulSizes', to='core.defaultsize'),
        ),
    ]
