from xml.etree.ElementInclude import include
from django.urls import path

from . import views

urlpatterns = [

    path("", views.index, name="index"),
    path("wiki/<str:entry>", views.entry, name="entry"),
    path("newPage", views.newPage, name="newPage"),
    path("wiki/<str:entry>/edit", views.edit, name="edit"),
    path("random", views.random, name="random"),
    path("search", views.search, name="search")
]
