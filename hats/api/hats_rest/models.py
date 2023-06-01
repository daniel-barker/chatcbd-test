from django.db import models
from django.urls import reverse


class LocationVO(models.Model):
    closet_name = models.CharField(max_length=200)
    section_number = models.PositiveSmallIntegerField()
    shelf_number = models.PositiveSmallIntegerField()
    location_href = models.CharField(max_length=200)


class Hat(models.Model):
    fabric = models.CharField(max_length=100)
    style_name = models.Charfield(max_length=100)
    color = models.CharField(max_length=100)
    picture_URL = models.CharField(max_length=100)
    wardrobe_location = models.CharField(max_length=100)

    def get_api_url(self):
        return reverse("api_location", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.fabric} - {self.style_name}/{self.shelf_number}"

    class Meta:
        ordering = ("fabric", "style_name", "shelf_number")
