from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Book
from mptt_tree_editor.admin import TreeEditor

class BookAdmin(TreeEditor):
    pass

admin.site.register(Book, TreeEditor)
