from django.conf.urls.defaults import *
import settings

urlpatterns = patterns('documents.views',
    # Ordinary views 
    (r'^$', 'index'),
    (r'^(?P<document_id>\d+)/$', 'detail'),
    (r'^add/$', 'add'),
    )
if settings.DEBUG:
    urlpatterns += patterns('',
                            (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
                            )

 
