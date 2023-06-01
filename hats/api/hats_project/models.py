from django.db import models
from django.urls import reverse


class LocationVO(models.Model):
    closet_name = models.CharField(max_length=200)
    section_number = models.PositiveSmallIntegerField())
    shelf_number = models.PositiveSmallIntegerField()

class Hat(models.Model):

    fabric = models.CharField(max_length=100)
    style_name = models.Charfield(max_length=100)
    color = models.CharField(max_length=100)
    picture_URL = models.CharField(max_length=100)
    wardrobe_location = models.CharField(max_length=100)

    def get_api_url(self):
        return reverse("api_location", kwargs={"pk": self.pk})
