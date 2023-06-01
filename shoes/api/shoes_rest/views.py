from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json
from common.json import ModelEncoder
from .models import BinVO, Shoe

class BinVOEncoder(ModelEncoder):
    model = BinVO
    properties = [
        "href",
        "closet_name",

    ]

class ShoeListEncoder(ModelEncoder):
    model = Shoe
    properties = [
        "shoe_make",
        "shoe_model",
    ]
    def get_extra_data(self, o):
        return {"bin": o.bin.closet_name}

class ShoeDetailEncoder(ModelEncoder):
    model = Shoe
    properties = [
        "shoe_make",
        "shoe_model",
        "shoe_color",
        "shoe_picture",
        "shoe_bin_location",
    ]
    encoders = {
        "bin": BinVOEncoder(),
    }



@require_http_methods(["GET", "POST"])
def api_list_shoes(request, bin_vo_id=None):

    if request.method == "GET":
        if bin_vo_id==None:
            shoes = Shoe.objects.all()
        else:
            shoes = Shoe.objects.filter(bin=bin_vo_id)
        return JsonResponse(
            {"shoes": shoes},
            encoder=ShoeListEncoder,
        )
    else:
        content = json.loads(request.body)

        try:
            bin_href = content["bin"]
            bin = BinVO.objects.get(import_href=bin_href)
            content["bin"] = bin
        except BinVO.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid bin id"},
                status=400,
            )

        shoe = Shoe.objects.create(**content)
        return JsonResponse(
            shoe,
            encoder=ShoeDetailEncoder,
            safe=False,
        )



@require_http_methods(["GET", "DELETE", "PUT"])
def api_show_shoe(request, pk):
    """
    Returns the details for the Attendee model specified
    by the pk parameter.

    This should return a dictionary with email, name,
    company name, created, and conference properties for
    the specified Attendee instance.

    {
        "email": the attendee's email,
        "name": the attendee's name,
        "company_name": the attendee's company's name,
        "created": the date/time when the record was created,
        "conference": {
            "name": the name of the conference,
            "href": the URL to the conference,
        }
    }
    """
    if request.method == "GET":
        try:
            shoe = Shoe.objects.get(id=pk)
            return JsonResponse(
                shoe,
                encoder=ShoeDetailEncoder,
                safe=False
            )
        except Shoe.DoesNotExist:
            response = JsonResponse({"message": "Does not exist"})
            response.status_code = 404
            return response
    elif request.method == "DELETE":
        try:
            count, _ =Shoe.objects.filter(id=pk).delete()
            return JsonResponse(
                {"Shoe has been removed from the database:": count > 0}
            )
        except Shoe.DoesNotExist:
            return JsonResponse({"message": "Shoe does not exist"})
    else: # PUT
        try:
            content = json.loads(request.body)
            shoe = Shoe.objects.get(id=pk)

            props = ["shoe_make", "shoe_model", "shoe_color", "shoe_picture"]
            for prop in props:
                if prop in content:
                    setattr(shoe, prop, content[prop])
            shoe.save()
            return JsonResponse(
                shoe,
                encoder=ShoeDetailEncoder,
                safe=False,
            )
        except Shoe.DoesNotExist:
            response = JsonResponse({"message": "Does not exist"})
            response.status_code = 404
            return response
        except KeyError:
            response = JsonResponse({"message": "Invalid/missing attribute"})
            response.status_code = 400
            return response
