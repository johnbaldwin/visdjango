from django.shortcuts import render

def index(request):
    return render(request, 'intro/index.html')

def svg_shapes(request):
    return render(request, 'intro/01_svg_shapes.html')

def d3_selection(request):
  return render(request, 'intro/02_d3_selection.html')

def d3_transition(request):
  return render(request, 'intro/03_d3_transition.html')

def d3_data_binding(request):
  return render(request, 'intro/04_d3_data_binding.html')