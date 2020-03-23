from django.contrib import admin

from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'cover', 'author','genre', 'condition', 'type', 'cost', 'pages']
