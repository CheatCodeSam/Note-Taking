from django.contrib import admin

from . import models


@admin.register(models.Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at")
    readonly_fields = (
        "id",
        "created_at",
    )
