from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.entry, name="entry"),
    path("<str:title>", views.SearchListView, name="search_list_view")
]
