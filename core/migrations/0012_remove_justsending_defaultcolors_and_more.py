# Generated by Django 5.0.4 on 2024-04-22 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_justsending_defaultsizes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='justsending',
            name='defaultColors',
        ),
        migrations.RemoveField(
            model_name='justsending',
            name='defaultProductTypes',
        ),
        migrations.RemoveField(
            model_name='justsending',
            name='defaultSizes',
        ),
        migrations.AddField(
            model_name='justsending',
            name='colors',
            field=models.CharField(choices=[('red', 'Red'), ('blue', 'Blue'), ('green', 'Green')], default='red', max_length=50),
        ),
        migrations.DeleteModel(
            name='DefaultColor',
        ),
        migrations.DeleteModel(
            name='DefaultProductType',
        ),
        migrations.DeleteModel(
            name='DefaultSize',
        ),
    ]