# Generated by Django 3.1 on 2020-08-08 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weddinglist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wedding_list',
            name='product_qty_ordered',
            field=models.FloatField(),
        ),
    ]
