"""
/catalog/ urls're here.
"""

from django.urls import path, re_path
from catalog import views
from catalog.views import BookListView, BookDetailView, AuthorListView, AuthorDetailView

urlpatterns = [
    re_path(r"^$", views.index, name="index"),
    # Book info
    re_path(r"^books/$", BookListView.as_view(), name="books"),
    re_path(r"^book/(?P<pk>\d+)$", BookDetailView.as_view(), name="book-detail"),
    # Author info
    re_path(r"^authors/$", AuthorListView.as_view(), name="authors"),
    re_path(r"^author/(?P<pk>\d+)$", AuthorDetailView.as_view(), name="author-detail"),
]
