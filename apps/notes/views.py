from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

from .models import Note


class ArticleDetailView(DetailView):
    model = Note
    template_name = "apps/notes/detail.html"
    pk_url_kwarg = "shortuuid"


class NoteCreateView(CreateView):
    template_name = "apps/notes/form.html"
    model = Note
    fields = ["title", "content"]

    def get_success_url(self):
        return reverse("apps:note-detail", kwargs={"shortuuid": self.object.id})
