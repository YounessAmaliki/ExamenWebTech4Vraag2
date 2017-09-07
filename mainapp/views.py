from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .form import adding
import json

# Create your views here.
def index(request):
    addjson = adding()
    
    
    if 'submit' in request.POST:
        data2 = {}
        with open('/Users/kiosk/Desktop/inhaalex/mainapp/data.json') as data_file:    
             data2 = json.load(data_file.decode("utf-8"))
             

        
        addjson = adding(request.POST)
        data = {}
        data['naam'] = addjson.cleaned_data['nnaam']
        data['reden'] = addjson.cleaned_data['ncalorieen']
        data['datum'] = addjson.cleaned_data['ningredienten']
        data['examen'] = addjson.cleaned_data['ntijd']
        json_data = json.dumps(data) 
        with open('/Users/kiosk/Desktop/inhaalex/mainapp/data.json', 'w') as outfile:
            json.dump(json_data, outfile)
    
    
    
    return render(request, 'index.html', {'addjson': addjson})