from django.db import models
from django.urls import reverse
from shortuuid.django_fields import ShortUUIDField


class Note(models.Model):
    id = ShortUUIDField(
        length=16,
        max_length=40,
        primary_key=True,
    )
    title = models.CharField(max_length=30, null=False, blank=True)
    content = models.TextField(
        null=False,
        blank=False,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("apps:note-detail", kwargs={"shortuuid": self.id})
