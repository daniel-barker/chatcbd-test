from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json

from common.json import ModelEncoder
from .models import BinVO, Shoe

class BinVOEncoder(ModelEncoder):
    model = BinVO
    properties = [

    ]

class ShoeListEncoder(ModelEncoder):
    model = Shoe
    properties = [
        "shoe_make",
        "shoe_model",
    ]

    def get_extra_data(self, o):
        return {"conference": o.conference.name}

class ShoeDetailEncoder(ModelEncoder):
    model = Shoe
    properties = [
        "email",
        "name",
        "company_name",
        "created",
        "conference",
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

        # Get the Conference object and put it in the content dict
        try:
            conference_href = content["conference"]
            conference = BinVO.objects.get(import_href=conference_href)
            content["conference"] = conference
        except ConferenceVO.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid conference id"},
                status=400,
            )

        attendee = Attendee.objects.create(**content)
        return JsonResponse(
            attendee,
            encoder=AttendeeDetailEncoder,
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
    attendee = Attendee.objects.get(id=pk)
    return JsonResponse(
        attendee,
        encoder=AttendeeDetailEncoder,
        safe=False,
    )
