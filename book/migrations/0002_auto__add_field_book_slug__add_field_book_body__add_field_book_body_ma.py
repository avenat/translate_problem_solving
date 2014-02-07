# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Book.slug'
        db.add_column(u'book_book', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default=datetime.datetime(2014, 2, 7, 0, 0), max_length=100),
                      keep_default=False)

        # Adding field 'Book.body'
        db.add_column(u'book_book', 'body',
                      self.gf('markupfield.fields.MarkupField')(default=1, rendered_field=True),
                      keep_default=False)

        # Adding field 'Book.body_markup_type'
        db.add_column(u'book_book', 'body_markup_type',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=30),
                      keep_default=False)

        # Adding field 'Book._body_rendered'
        db.add_column(u'book_book', '_body_rendered',
                      self.gf('django.db.models.fields.TextField')(default=1),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Book.slug'
        db.delete_column(u'book_book', 'slug')

        # Deleting field 'Book.body'
        db.delete_column(u'book_book', 'body')

        # Deleting field 'Book.body_markup_type'
        db.delete_column(u'book_book', 'body_markup_type')

        # Deleting field 'Book._body_rendered'
        db.delete_column(u'book_book', '_body_rendered')


    models = {
        u'book.book': {
            'Meta': {'object_name': 'Book'},
            '_body_rendered': ('django.db.models.fields.TextField', [], {}),
            'body': ('markupfield.fields.MarkupField', [], {'rendered_field': 'True'}),
            'body_markup_type': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['book']