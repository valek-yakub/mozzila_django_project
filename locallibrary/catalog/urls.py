"""
/catalog/ urls're here.
"""

from django.urls import path, re_path
from catalog import views
from catalog.views import BookListView, BookDetailView

urlpatterns = [
    re_path(r"^$", views.index, name="index"),
    re_path(r"^books/$", BookListView.as_view(), name="books"),
    re_path(r"^book/(?P<pk>\d+)$", BookDetailView.as_view(), name="book-detail"),
]
