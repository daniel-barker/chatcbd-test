from django.contrib import admin
from wardrobe_api.models import Location, Bin


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "closet_name",
        "section_number",
        "shelf_number",

    )


@admin.register(Bin)
class BinAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "closet_name",
        "bin_number",
        "bin_size",
    )
