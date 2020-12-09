from django.contrib import admin

# Register your models here.
from catalog.models import Author, Book, Genre, BookInstance, Language

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)

