import django
import os
import sys
import time
import json
import requests

sys.path.append("")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hats_project.settings")
django.setup()


from hats_rest.models import LocationVO


def locations_storage():
    response = requests.get("http://wardrobe-api:8000/api/locations")
    content = json.loads(response.content)
    for location in content["locations"]:
        LocationVO.objects.update_or_create(
            location_href=location["href"],
            defaults={
                "closet_name": location["closet_name"],
                # "section_number": location["section_number"],
                # "shelf_number": location["shelf_number"],
            }
        )


def poll():
    while True:
        print('Hats poller polling for data')
        try:
            locations_storage()
        except Exception as e:
            print(e, file=sys.stderr)
        time.sleep(60)


if __name__ == "__main__":
    poll()
