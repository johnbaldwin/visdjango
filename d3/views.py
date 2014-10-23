from django.shortcuts import render
from django.http import HttpResponse
import os
import json
import csv

def index(request):
    return render(request, 'd3/index.html')

#
# Example pages
#

def shapes(request):
    return render(request, 'd3/shapes.html')

def barchart(request):
    return render(request, 'd3/barchart.html')

def scatterplot(request):
    return render(request, 'd3/scatterplot.html')

def scatterplot_2(request):
    return render(request, 'd3/scatterplot_2.html')

#
# AJAX Actions
#

def shapes_data(request):

    response_data = [
        { "x_axis": 30,  "y_axis":  30, "radius": 20, "color": "green" },
        { "x_axis": 70,  "y_axis":  70, "radius": 20, "color": "green" },
        { "x_axis": 110, "y_axis": 100, "radius": 20, "color": "green" }
    ]

    return HttpResponse(json.dumps(response_data), content_type = 'application/json')

# The following two methods are just to demonstrate the AJAX call from D3
# TODO: for demo purposes, merge these into one method and get request parameters

def letter_frequency_data(request):
    os.getcwd()  # Should get this Django project root (where manage.py is)
    fn = os.path.abspath(os.path.join(os.getcwd(),'d3/data/letter_frequency.tsv'))
    # TODO: Move to helper module
    response_data = {}
    data_format = 'tsv'
    if data_format == 'json':
        with open(fn, 'rb') as tsvin:
            tsvin = csv.reader(tsvin, delimiter='\t')

            for row in tsvin:
                print 'col1 = %s  col2 = %s' % (row[0], row[1])
                response_data[row[0]] = row[1]
        result = HttpResponse(json.dumps(response_data), content_type = 'application/json')
    else:
        with open(fn, 'rb') as tsvin:
            buff = tsvin.read()
        result = HttpResponse(buff, content_type = 'text/tsv')

    return result


def scatterplot_data(request):
    # TODO: add params checking
    fn = os.path.abspath(os.path.join(os.getcwd(),'data/scatterplot.tsv'))
    with open(fn, 'rb') as tsvin:
        buff = tsvin.read()
        result = HttpResponse(buff, content_type = 'text/tsv')
    return result


def example_json_data_response(request):
    """Return JSON data, demonstrates AJAX call
    This is a very simple method that returns hardcoded values.

    """

    # Build our response dictionary
    response_data = {
        'alpha':'first letter',
        'bravo':'second letter',
    }

    return HttpResponse(json.dumps(response_data), content_type = 'application/json')
