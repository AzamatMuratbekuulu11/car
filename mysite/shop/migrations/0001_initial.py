# Generated by Django 5.0.6 on 2024-05-28 05:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_category', models.CharField(max_length=16, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Marka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_marka', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_model', models.CharField(max_length=32, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_car', models.CharField(max_length=32)),
                ('price', models.PositiveSmallIntegerField(default=1)),
                ('description', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('year', models.SmallIntegerField()),
                ('image', models.ImageField(upload_to='images/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category')),
                ('marka', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.marka')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.model')),
            ],
        ),
    ]