from django.urls import path

from . import views

urlpatterns = [
    path("<str:shortuuid>/", views.ArticleDetailView.as_view(), name="note-detail"),
    path("", views.NoteCreateView.as_view(), name="note-create"),
]
