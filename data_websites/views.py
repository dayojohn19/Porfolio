from django.shortcuts import render
from .models import WebsiteMessages
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.http import JsonResponse
import json


def index(request):
    return render(request, 'data/websites/index.html')


@csrf_exempt
def postMessage(request):
    if request.method == "POST":
        PostedData = json.loads(request.body)
        PostedMessage = PostedData.get("message")
        PostedUser = PostedData.get("from")
        WebsiteMessages.objects.create(
            message=PostedMessage, sender=PostedUser)

        return JsonResponse(PostedData)
        return print('\n DONE: ', PostedData, '\n by: ', PostedUser, '\n ')

    else:
        allMessages = WebsiteMessages.objects.all()
        return JsonResponse([message.serialize() for message in allMessages], safe=False)