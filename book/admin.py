from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Book
from mptt_tree_editor.admin import TreeEditor
from django.db import models
from epiceditor.widgets import AdminEpicEditorWidget

class BookAdmin(TreeEditor):
    formfield_overrides = {
            models.TextField: {'widget': AdminEpicEditorWidget },
    }

admin.site.register(Book, BookAdmin)
