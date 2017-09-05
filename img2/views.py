from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from img2 import imggrab

@csrf_exempt  # The communication isn't over HTTPS, so this is necessary so that Django doesn't freak out

def index(request):
    criteria = str(request.body)
    s = criteria.find("text")  # s for start
    s = s + 5
    e = criteria.find("&response_url")  # e for end
    criteria = criteria[s:e]

    result = imggrab.find(criteria)  # searches for the image

    imgJSON = {
        "response_type": "in_channel",
        "attachments": [
            {
                "text": "",
                "image_url": result,
                "color": "#764FA5"
            }
        ]
    }

    if type(result) is not dict:  # is the response a dictionary (failed), or just the link?
        return JsonResponse(imgJSON)

    else:
        return JsonResponse(result)
