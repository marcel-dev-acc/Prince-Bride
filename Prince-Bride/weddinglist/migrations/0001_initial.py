# Generated by Django 3.1 on 2020-08-08 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='wedding_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_list', models.IntegerField()),
                ('product_id', models.IntegerField()),
                ('product_name', models.CharField(max_length=200)),
                ('product_brand', models.CharField(max_length=200)),
                ('product_price', models.FloatField()),
                ('product_qty_ordered', models.IntegerField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]