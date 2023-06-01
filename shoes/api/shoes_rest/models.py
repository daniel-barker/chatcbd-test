from django.db import models
from django.urls import reverse

# Create your models here.

class BinVO(models.Model):

    idkyet = models.CharField

class Shoe(models.Model):

    make = models.CharField(max_length=100)
    model = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    picture = models.URLField()

    bin = models.ForeignKey(
        BinVO,
        related_name="shoes",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

    def get_api_url(self):
        return reverse("api_show_attendee", kwargs={"pk": self.pk})
