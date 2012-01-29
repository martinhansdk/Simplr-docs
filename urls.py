from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # Ordinary views 
    (r'^', include('documents.urls')),
)
