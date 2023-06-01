# Generated by Django 4.0.3 on 2023-06-01 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BinVO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('closet_name', models.CharField(max_length=100)),
                ('bin_number', models.PositiveSmallIntegerField()),
                ('bin_size', models.PositiveSmallIntegerField()),
                ('bin_href', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Shoe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shoe_make', models.CharField(max_length=100)),
                ('shoe_model', models.CharField(max_length=200)),
                ('shoe_color', models.CharField(max_length=200)),
                ('shoe_picture', models.URLField()),
                ('shoe_bin_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shoe_bin_location', to='shoes_rest.binvo')),
            ],
        ),
    ]
