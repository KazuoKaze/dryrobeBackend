# Generated by Django 5.0.4 on 2024-04-26 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_remove_justsending_productimage2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='justsending',
            name='defaultSize',
            field=models.CharField(choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('8', '8'), ('10', '10'), ('12', '12'), ('14', '14'), ('16', '16'), ('One Size', 'One Size')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='justsending',
            name='defaultproductType',
            field=models.CharField(choices=[('Adapt', 'Adapt'), ('Boots & Mittens', 'Boots & Mittens'), ('Dryrobe® Advance', 'Dryrobe® Advance'), ('Headwear', 'Headwear'), ('Lite', 'Lite'), ('Towel Change Robes', 'Towel Change Robes')], default='', max_length=50),
        ),
    ]