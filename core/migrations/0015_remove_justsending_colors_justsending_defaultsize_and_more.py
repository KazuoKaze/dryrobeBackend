# Generated by Django 5.0.4 on 2024-04-22 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_remove_justsending_color_justsending_colors_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='justsending',
            name='colors',
        ),
        migrations.AddField(
            model_name='justsending',
            name='defaultSize',
            field=models.CharField(choices=[('s', 'S'), ('m', 'M'), ('l', 'L'), ('XL', 'XL'), ('8s', '8'), ('10s', '10'), ('12s', '12'), ('14s', '14'), ('16s', '16'), ('one Size', 'One Size')], default='', max_length=50),
        ),
        migrations.AddField(
            model_name='justsending',
            name='defaultcolors',
            field=models.CharField(choices=[('black', 'Black'), ('blue', 'Blue'), ('camo', 'Camo'), ('green', 'Green'), ('gray', 'Gray'), ('orange', 'Orange'), ('pink', 'Pink'), ('purple', 'Purple')], default='', max_length=50),
        ),
        migrations.AddField(
            model_name='justsending',
            name='defaultproductType',
            field=models.CharField(choices=[('adapt', 'Adapt'), ('boots', 'Boots & Mittens'), ('advance', 'Dryrobe® Advance'), ('headwear', 'Headwear'), ('lite', 'Lite'), ('towel', 'Towel Change Robes'), ('pink', 'Pink'), ('purple', 'Purple')], default='', max_length=50),
        ),
    ]
