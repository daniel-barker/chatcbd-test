from django.db import models


# Create your models here.

class BinVO(models.Model):
    closet_name = models.CharField(max_length=100, null=True)
    bin_number = models.PositiveSmallIntegerField()
    bin_size = models.PositiveSmallIntegerField()
    bin_href = models.CharField(max_length=100, unique=True)


class Shoe(models.Model):

    shoe_make = models.CharField(max_length=100, null=True)
    shoe_model = models.CharField(max_length=200, null=True)
    shoe_color = models.CharField(max_length=200, null=True)
    shoe_picture = models.URLField(null=True)

    bin = models.ForeignKey(
        BinVO,
        related_name="shoe_bin_location",
        on_delete=models.CASCADE,
    )

