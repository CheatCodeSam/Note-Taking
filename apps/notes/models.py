from django.db import models
from shortuuid.django_fields import ShortUUIDField


class Note(models.Model):
    id = ShortUUIDField(
        length=16,
        max_length=40,
        primary_key=True,
    )
    title = models.CharField(max_length=30, null=False, blank=True)
    content = models.TextField(
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return self.title
