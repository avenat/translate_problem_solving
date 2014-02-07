# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Book.parent'
        db.add_column(u'book_book', 'parent',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='child', null=True, to=orm['book.Book']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Book.parent'
        db.delete_column(u'book_book', 'parent_id')


    models = {
        u'book.book': {
            'Meta': {'object_name': 'Book'},
            '_body_rendered': ('django.db.models.fields.TextField', [], {}),
            'body': ('markupfield.fields.MarkupField', [], {'rendered_field': 'True'}),
            'body_markup_type': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'child'", 'null': 'True', 'to': u"orm['book.Book']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['book']