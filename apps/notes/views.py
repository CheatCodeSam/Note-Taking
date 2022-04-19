from django.shortcuts import get_object_or_404
from .models import Note
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.urls import reverse


def detail(request, shortuuid):
    note = get_object_or_404(Note, pk=shortuuid)
    return render(request, "apps/notes/detail.html", {"note": note})


class NoteCreateView(CreateView):
    template_name = "apps/notes/form.html"
    model = Note
    fields = ["title", "content"]

    def get_success_url(self):
        return reverse("apps:note-detail", kwargs={"shortuuid": self.object.id})
