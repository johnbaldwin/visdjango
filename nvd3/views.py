from django.shortcuts import render
from django.http import HttpResponse

import json


def index(request):
    return render(request, 'nvd3/index.html')

def piechart(request):
    return render(request, 'nvd3/piechart.html')

def barchart_1(request):
    return render(request, 'nvd3/barchart_1.html')

def barchart_2(request):
    return render(request, 'nvd3/barchart_2.html')

#
# Data
#

def barchart_data(request):

    response_data = [
        {
          "key": "Cumulative Return",
          "values": [
            { "label" : "A Label", "value" : -29.765957771107 } ,
            { "label" : "B Label", "value" : 0                } ,
            { "label" : "C Label", "value" : 32.807804682612  } ,
            { "label" : "D Label", "value" : 196.45946739256  } ,
            { "label" : "E Label", "value" : 0.19434030906893 } ,
            { "label" : "F Label", "value" : -98.079782601442 } ,
            { "label" : "G Label", "value" : -13.925743130903 } ,
            { "label" : "H Label", "value" : -5.1387322875705 }
          ]
        }
    ]
    return HttpResponse(json.dumps(response_data), content_type = 'application/json')
