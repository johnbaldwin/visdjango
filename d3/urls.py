# d3 urls
from django.conf.urls import patterns, url

from d3 import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='d3-index'),
  # TODO: This is repetitive, figure out how to DRY it up
  url(r'^shapes/', views.shapes, name='d3-shapes'),
  url(r'^barchart/', views.barchart, name='d3-barchart'),
  url(r'^scatterplot/', views.scatterplot, name='d3-scatterplot'),
  url(r'^scatterplot-2/', views.scatterplot_2, name='d3-scatterplot-2'),

  #
  # Data resources
  #

  # TODO: Verify we probably don't need to name this since we won't link from it in a page
  url(r'^shapes-data/', views.shapes_data),
  url(r'^letter-frequency-data/', views.letter_frequency_data),
  url(r'^scatterplot_data/$', views.scatterplot_data, name='d3-scatterplot-2-data'),

)