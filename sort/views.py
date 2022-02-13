from django.http.response import HttpResponse
from django.shortcuts import render
from sawo import createTemplate, getContext, verifyToken
import json
import os
from .models import Config

# Create your views here.

def index(request):
    return render(request,"pages/index.html")


load = ''
loaded = 0


def setPayload(payload):
    global load
    load = payload

def setLoaded(reset=False):
    global loaded
    if reset:
        loaded=0
    else:
        loaded+=1

createTemplate("partials")


def login(request):
    config = Config.objects.order_by('-api_key')[:1]
    setLoaded()
    setPayload(load if loaded<2 else '')
    # print(config('api_key'))
    # configuration = {
    #             "auth_key": os.environ.get(Config.api_key),
    #             "identifier": "email",
    #             "to": "receive"
    # }
    context = {"sawo":getContext(config ,"receive/") if(config) else {}, "load":load,"title":"Home"}
    
    return render(request,"pages/login.html", context)

def receive(request):
    if request.method == 'POST':
        payload = json.loads(request.body)["payload"]
        print("*"*50)
        setLoaded(True)
        setPayload(payload)
        print(payload)
        
        status = 200 if verifyToken(payload) else 404
        print(status)
        response_data = {"status":status}
        return HttpResponse(json.dumps(response_data), content_type="application/json")
