from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Book
from mptt_tree_editor.admin import TreeEditor
from pagedown.widgets import AdminPagedownWidget
from django.db import models

class BookAdmin(TreeEditor):
    formfield_overrides = {
            models.TextField: {'widget': AdminPagedownWidget },
    }

admin.site.register(Book, BookAdmin)
