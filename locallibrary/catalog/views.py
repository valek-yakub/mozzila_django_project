from django.shortcuts import render

# Create your views here.
from catalog.models import Book, BookInstance, Author


def index(request):
    """
        Display func for the home page of the site.
    :param request:
    :return:
    """
    # Generates numbers of some main objects.
    num_books = Book.objects.count()  # Method "all()" is applied by default.
    num_instances = BookInstance.objects.count()

    # Available books ( status = 'a')
    num_instance_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()

    # Rendering HTML template 'index.html' with data are inside
    # 'context' variable.
    return render(
        request,
        "index.html",
        context={
            'num_books': num_books,
            'num_instances': num_instances,
            'num_instances_available': num_instance_available,
            'num_author': num_authors
        }
    )
