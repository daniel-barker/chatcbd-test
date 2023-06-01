from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from common.json import ModelEncoder
from models import Hat
import json


class HatListEncoder(ModelEncoder):
    model = Hat
    properties = ["name"]


class HatDetailEncoder(ModelEncoder):
    model = Hat
    properties = [
        "fabric",
        "style_name",
        "color",
        "picture_url",
        "location",
    ]


@require_http_methods(["GET", "POST"])
def api_list_hats(request):
    """
    Lists the hat names and the link to the hat.

    Returns a dictionary with a single key "hats" which
    is a list of hat names and URLS. Each entry in the list
    is a dictionary that contains the name of the hat and
    the link to the hat's information.

    {
        "hats": [
            {
                "name": hat's name,
                "href": URL to the hat,
            },
            ...
        ]
    }
    """
    if request.method == "GET":
        hats = Hat.objects.all()
        return JsonResponse(
            {"hats": hats},
            encoder=HatListEncoder,
        )
    # else:
    #     content = json.loads(request.body)

        # photo = get_photo(content["city"], content["state"].abbreviation)
        # content.update(photo)
        # hat = Hat.objects.create(**content)
        # return JsonResponse(
        #     hat,
        #     encoder=HatDetailEncoder,
        #     safe=False,
        # )


@require_http_methods(["DELETE", "GET", "PUT"])
def api_show_hat(request, pk):
    """
    Returns the details for the hat model specified
    by the pk parameter.

    This should return a dictionary with the name, city,
    room count, created, updated, and state abbreviation.

    {
        "name": hat's name,
        "city": hat's city,
        "room_count": the number of rooms available,
        "created": the date/time when the record was created,
        "updated": the date/time when the record was updated,
        "state": the two-letter abbreviation for the state,
    }
    """
    if request.method == "GET":
        hat = Hat.objects.get(id=pk)
        return JsonResponse(
            hat,
            encoder=HatDetailEncoder,
            safe=False,
        )
    elif request.method == "DELETE":
        count, _ = Hat.objects.filter(id=pk).delete()
        return JsonResponse({"deleted": count > 0})
    else:
        content = json.loads(request.body)
        Hat.objects.filter(id=pk).update(**content)
        hat = Hat.objects.get(id=pk)
        return JsonResponse(
            hat,
            encoder=HatDetailEncoder,
        )
