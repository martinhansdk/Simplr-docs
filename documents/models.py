from django.db import models
import tagging

class Document(models.Model):
    title = models.CharField(max_length=500)
    filename = models.CharField(max_length=500)
    description = models.TextField()

    def __unicode__(self):
        return self.title

tagging.register(Document)

