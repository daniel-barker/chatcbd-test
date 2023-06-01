from django.contrib import admin
from wardrobe_api.models import Location, Bin
# Register your models here.
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "closet_name",
        "section_number",
        "shelf_number",

    )
