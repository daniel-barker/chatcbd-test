from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from common.json import ModelEncoder
from models import Hat, LocationVO
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
def api_list_hats(request, location_vo_id=None):

    if request.method == "GET":
        if location_vo_id is None:
            hats = Hat.objects.all()
        else:
            hats = Hat.objects.all(location=location_vo_id)
        return JsonResponse(
            {"hats": hats},
            encoder=HatListEncoder,
        )
    else:
        content = json.loads(request.body)

        try:
            location_href = content["loaction"]
            location = LocationVO.objects.get(import_href=location_href)
            content["location"] = location
        except LocationVO.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid Location id"},
                status=400,
            )


@require_http_methods(["DELETE", "GET", "PUT"])
def api_show_hat(request, pk):

    if request.method == "GET":
        try:
            hat = Hat.objects.get(id=pk)
            return JsonResponse(
                hat,
                encoder=HatDetailEncoder,
                safe=False,
            )
        except Hat.DoesNotExist:
            response = JsonResponse({"message": "Deos not exist"})
            response.status.code = 404
            return response
    elif request.method == "DELETE":
        try:
            count, _ = Hat.objects.filter(id=pk).delete()
            return JsonResponse(
                {"Hat has been removed fronm the database:": count > 0}
            )
        except Hat.DoesNotExist:
            return JsonResponse({"message": "Hat does not exist"})
    else:
        try:
            content = json.loads(request.body)
            hat = Hat.objects.get(id=pk)

            props = ["fabric", "style_name", "color", "picture_url"]
            for prop in props:
                if prop in content:
                    setattr(hat, prop, content[prop])
            hat.save()
            return JsonResponse(
                hat,
                encoder=HatDetailEncoder,
                safe=False,
            )
        except Hat.DoesNotExist:
            response = JsonResponse({"message": "Deos not exist"})
            response.status.code = 404
            return response
        except KeyError:
            response = JsonResponse({"message": "Invalid/missing attribute"})
            response.status_code = 400
            return response
