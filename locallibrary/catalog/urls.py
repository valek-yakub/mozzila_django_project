"""
/catalog/ urls're here.
"""

from django.urls import path
from catalog import views


urlpatterns = [
    path("", views.index, name="index"),
]
