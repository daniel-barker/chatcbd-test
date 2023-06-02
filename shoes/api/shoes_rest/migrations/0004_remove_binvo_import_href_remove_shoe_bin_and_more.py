# Generated by Django 4.0.3 on 2023-06-02 02:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shoes_rest', '0003_remove_binvo_bin_href_remove_shoe_shoe_bin_location_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='binvo',
            name='import_href',
        ),
        migrations.RemoveField(
            model_name='shoe',
            name='bin',
        ),
        migrations.RemoveField(
            model_name='shoe',
            name='color',
        ),
        migrations.RemoveField(
            model_name='shoe',
            name='manufacturer',
        ),
        migrations.RemoveField(
            model_name='shoe',
            name='model_name',
        ),
        migrations.RemoveField(
            model_name='shoe',
            name='picture_url',
        ),
        migrations.AddField(
            model_name='binvo',
            name='bin_href',
            field=models.CharField(default=1, max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shoe',
            name='shoe_bin_location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='shoe_bin_location', to='shoes_rest.binvo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shoe',
            name='shoe_color',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='shoe',
            name='shoe_make',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='shoe',
            name='shoe_model',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='shoe',
            name='shoe_picture',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='binvo',
            name='bin_number',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='binvo',
            name='bin_size',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]