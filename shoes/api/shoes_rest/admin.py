from django.contrib import admin
from shoes_rest.models import Shoe, BinVO
# Register your models here.
@admin.register(Shoe)
class ShoeAdmin(admin.ModelAdmin):
    list_display = (
        "shoe_make",
        "shoe_model"
    )
