# Generated by Django 5.0.4 on 2024-04-20 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='justsending',
            name='bio',
            field=models.CharField(blank=True, max_length=99999, null=True),
        ),
        migrations.AlterField(
            model_name='justsending',
            name='bio2',
            field=models.CharField(blank=True, max_length=99999, null=True),
        ),
        migrations.AlterField(
            model_name='justsending',
            name='bio3',
            field=models.CharField(blank=True, max_length=99999, null=True),
        ),
        migrations.AlterField(
            model_name='justsending',
            name='bio4',
            field=models.CharField(blank=True, max_length=99999, null=True),
        ),
    ]
