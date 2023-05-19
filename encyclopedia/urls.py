from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>", views.entry_page, name="entry_page"),
    path("search_results", views.search, name="results"),
    path("create_new/", views.create_entry, name ="create_new"),
    path("edit", views.edit, name="edit"),
    path("save_edit",views.save_edit, name= "save_edit"),
    path("random_page",views.random_page, name = "random_page"),
    path("<entry_name>", views.entry , name = "entry")
]
