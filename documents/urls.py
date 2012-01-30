from django.conf.urls.defaults import *
import settings

urlpatterns = patterns('documents.views',
    # Ordinary views 
    (r'^$', 'index'),
    (r'^(?P<document_id>\d+)/$', 'detail'),
    (r'^add/$', 'add'),
    (r'^tag/([\w-]+)/$', 'tag'),
    )

# URLs for taggit_autocomplete_modified
urlpatterns += patterns('',
    url(r'^taggit_autocomplete_modified/', include('taggit_autocomplete_modified.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
                            (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
                            )

 
