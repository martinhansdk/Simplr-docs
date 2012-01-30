from django.db import models
from taggit_autocomplete_modified.managers import TaggableManagerAutocomplete as TaggableManager

class Document(models.Model):
    title = models.CharField(max_length=500)
    filename = models.FileField(upload_to='uploads')
    description = models.TextField()
    tags = TaggableManager()

    def __unicode__(self):
        return self.title



