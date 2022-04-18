from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Note


from django.shortcuts import render


def index(request, shortuuid):
    note = get_object_or_404(Note, pk=shortuuid)
    return render(request, "apps/notes/index.html", {"note": note})
