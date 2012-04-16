from django.conf.urls import patterns, url
from sample import views

urlpatterns = patterns('',
    url(r'^$', views.Index.as_view()),
)
