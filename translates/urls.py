from django.conf.urls import url
from . import views

app_name = 'translates'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new/$', views.new, name="new"),
    url(r'^create/$', views.create, name="create"),
    url(r'^(?P<text_id>[0-9]+)/(?P<sentence_id>[0-9]+)/$', views.interpret, name='interpret'),
]