from django.urls import path
from .views import detail, NoteCreateView

urlpatterns = [
    path("<str:shortuuid>/", detail, name="note-detail"),
    path("", NoteCreateView.as_view(), name="note-create"),
]
