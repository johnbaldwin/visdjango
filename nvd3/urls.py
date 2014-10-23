from django.conf.urls import patterns, url

from nvd3 import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='nvd3-index'),
  url(r'^piechart/', views.piechart, name='nvd3-piechart'),
  url(r'^barchart_1/', views.barchart_1, name='nvd3-barchart-1'),
  url(r'^barchart_2/', views.barchart_2, name='nvd3-barchart-2'),

  # data URLS
  url(r'^barchart_data/$', views.barchart_data),
)