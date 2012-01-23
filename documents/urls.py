from django.conf.urls.defaults import *

urlpatterns = patterns('documents.views',
    # Ordinary views 
    (r'^$', 'index'),
    (r'^(?P<document_id>\d+)/$', 'detail'),
    (r'^(?P<document_id>\d+)/add/$', 'add'),
)


