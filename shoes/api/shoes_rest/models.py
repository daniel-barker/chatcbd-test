from django.db import models
from django.urls import reverse

# Create your models here.

class BinVO(models.Model):

    closet_name = models.CharField(max_length=100)
    bin_number = models.PositiveSmallIntegerField()
    bin_size = models.PositiveSmallIntegerField()
    bin_href = models.CharField(max_length=100, unique=True)


class Shoe(models.Model):

    shoe_make = models.CharField(max_length=100)
    shoe_model = models.CharField(max_length=200)
    shoe_color = models.CharField(max_length=200)
    shoe_picture = models.URLField()

    shoe_bin_location = models.ForeignKey(
        BinVO,
        related_name="shoe_bin_location",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

    def get_api_url(self):
        return reverse("api_show_shoe", kwargs={"pk": self.pk})
