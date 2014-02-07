import mptt
from django.db import models
from markupfield.fields import MarkupField

class Book(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100)
    parent = models.ForeignKey('self', blank=True, null=True, verbose_name="Parent", related_name='child')
    body = MarkupField()


    def __unicode__(self):
        return self.title

mptt.register(Book,)
