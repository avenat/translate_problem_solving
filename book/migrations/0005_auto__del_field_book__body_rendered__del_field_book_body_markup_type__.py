# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Book._body_rendered'
        db.delete_column(u'book_book', '_body_rendered')

        # Deleting field 'Book.body_markup_type'
        db.delete_column(u'book_book', 'body_markup_type')


        # Changing field 'Book.body'
        db.alter_column(u'book_book', 'body', self.gf('django.db.models.fields.TextField')())

    def backwards(self, orm):
        # Adding field 'Book._body_rendered'
        db.add_column(u'book_book', '_body_rendered',
                      self.gf('django.db.models.fields.TextField')(default=1),
                      keep_default=False)

        # Adding field 'Book.body_markup_type'
        db.add_column(u'book_book', 'body_markup_type',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=30),
                      keep_default=False)


        # Changing field 'Book.body'
        db.alter_column(u'book_book', 'body', self.gf('markupfield.fields.MarkupField')(rendered_field=True))

    models = {
        u'book.book': {
            'Meta': {'object_name': 'Book'},
            'body': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'child'", 'null': 'True', 'to': u"orm['book.Book']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        }
    }

    complete_apps = ['book']