from django.core.management import BaseCommand
from django.utils.text import slugify

from catalog.models import Book


class Command(BaseCommand):

    def handle(self, *args, **options):
        books = Book.objects.all()
        for book in books:
            book.slug = slugify(book.title, allow_unicode=True)
        Book.objects.bulk_update(books, ["slug"], batch_size=4)
