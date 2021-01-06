from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from .models import Book, BookInstance, Author


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

    num_books_lookup = Book.objects.filter(title__icontains="divine").count()

    # Rendering HTML template 'index.html' with data are inside
    # 'context' variable.
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instance_available,
        'num_authors': num_authors,
        'num_books_lookup': num_books_lookup
    }

    return render(request, "index.html", context)


class BookListView(ListView):
    """
        View displays a list of all books.
    """
    model: Book = Book
    paginate_by = 10

    def get_queryset(self):
        # return Book.objects.filter(title__icontains="war")    # Получить 5 книг, содержащих 'war' в заголовке
        return Book.objects.prefetch_related("author")  # Все книги с полем авторов.

    def get_context_data(self, **kwargs):
        # В первую очередь получаем базовую реализацию контекста
        context = super(BookListView, self).get_context_data(**kwargs)
        # Добавляем новую переменную к контексту и иниуиализируем ее некоторым значением
        context['some_data'] = 'This is just some data'
        return context


class BookDetailView(DetailView):
    """
        View displays detail information about book.
    """

    model: Book = Book

    def get_queryset(self):
        book = Book.objects.prefetch_related("genre")
        return book


class AuthorListView(ListView):
    """
        View displays a list of all authors.
    """
    model: Author = Author
    paginate_by = 10

    # def get_queryset(self):
    #     # return Book.objects.filter(title__icontains="war")    # Получить 5 книг, содержащих 'war' в заголовке
    #     return Author.objects.prefetch_related("author")  # Все книги с полем авторов.

    def get_context_data(self, **kwargs):
        # В первую очередь получаем базовую реализацию контекста
        context = super(AuthorListView, self).get_context_data(**kwargs)
        # Добавляем новую переменную к контексту и иниуиализируем ее некоторым значением
        context['some_data'] = 'This is just some data'
        return context


class AuthorDetailView(DetailView):
    """
        View displays detail information about author.
    """

    model: Author = Author

    # def get_queryset(self):
    #     author = Author.objects.prefetch_related("book_set")
    #     return author
