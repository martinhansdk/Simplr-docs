from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponseRedirect
from django import forms

from documents.models import Document
from tagging.models import Tag


def index(request):
    return render_to_response('documents/index.html',
                              dict(documents = Document.objects.all().order_by('title'),
                                   tags = Tag.objects.all().order_by('name'),
                                   )
                              )

def detail(request, document_id):
    """If document_id is None, then this is a new document."""
    doc = None
    if document_id is not None:
        try:
            doc = Document.objects.get(pk=document_id)
        except Document.DoesNotExist:
            raise Http404
        

    if request.method == 'POST': # If the form has been submitted...
        cancel = request.POST.get('cancel', None)

        if cancel:
            return HttpResponseRedirect('/') 
        else:
            form = DocumentForm(request.POST, request.FILES, instance=doc) # A form bound to the POST data
            if form.is_valid(): # All validation rules pass
                form.save()
                return HttpResponseRedirect('/') # Redirect after POST
    else:
        form = DocumentForm(instance=doc) # An unbound form

    c = {
        'form': form,
        'doc' : doc,
    }
    c.update(csrf(request))

    return render_to_response('documents/detail.html', c)


def add(request):
    return detail(request, document_id=None)


def tag(request, tag):

    docs=Document.objects.filter(tags__slug__in=[ tag ])

    return render_to_response('documents/tag.html', dict(tag=tag,
                                                         docs=docs))

##### File handling #####

def handle_uploaded_file(f, name):
    destination = open('/home/martin/docunizer/uploads/'+name, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()

##### Forms #####

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document

