from django.conf.urls import patterns, url

from intro import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='intro-index'),
  url(r'^svg-shapes/',views.svg_shapes, name='intro-svg-shapes'),
  url(r'^d3-selection/', views.d3_selection, name='intro-d3-selection'),
  url(r'^d3-transition/', views.d3_transition, name='intro-d3-transition'),
  url(r'^d3-data-binding/', views.d3_data_binding, name='intro-d3-data-binding'),
)