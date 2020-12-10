from django.contrib import admin

# Register your models here.
from catalog.models import Author, Book, Genre, BookInstance, Language

admin.site.register(Genre)
admin.site.register(Language)


class BooksInstanceInline(admin.TabularInline):
    """
        Class represents book instances in the add/change menu of the Book.
    """
    model = BookInstance
    extra = 0  # No extra info from


class BooksInline(admin.StackedInline):
    """
            Class represents book instances in the add/change menu of the Author.
    """
    model = Book
    extra = 0
    fieldsets = (
        (None, {
            "fields": ("title", "genre"),
        }),
        ("Additional options", {
            "classes": ("collapse",),
            "fields": ("summary", "isbn", "languages")
        })
    )


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
        Class modifies Admin site for the Book model.
    """
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    """
        Class modifies Admin site for the BookInstance model.
    """
    list_display = ('book', 'status', 'due_back', 'id')
    list_filter = ('due_back', 'status')
    fieldsets = (
        (None, {
            "fields": ("book", "imprint", "id")
        }),
        ("Availability", {
            "fields": ("due_back", "status")
        }),
    )


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """
        Class modifies Admin site for the Author model.
    """
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]
