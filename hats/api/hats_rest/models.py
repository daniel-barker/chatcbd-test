from django.db import models


class LocationVO(models.Model):
    closet_name = models.CharField(max_length=200)
    section_number = models.PositiveSmallIntegerField()
    shelf_number = models.PositiveSmallIntegerField()
    location_href = models.CharField(max_length=200)


class Hat(models.Model):
    fabric = models.CharField(max_length=100)
    style_name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    picture_url = models.CharField(max_length=100)

    location = models.ForeignKey(
        LocationVO,
        related_name="hat_location",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.fabric} - {self.style_name}/{self.shelf_number}"
