# Generated by Django 4.0.3 on 2023-06-02 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hats_rest', '0002_rename_picture_url_hat_picture_url_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='locationvo',
            name='section_number',
        ),
        migrations.RemoveField(
            model_name='locationvo',
            name='shelf_number',
        ),
    ]
