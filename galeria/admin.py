# admin.py
from django.contrib import admin
from .models import IATool

@admin.register(IATool)
class IAToolAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "categoria", "publicada", "data_publicacao")
    list_display_links = ("id", "nome")
    search_fields = ("nome", "categoria")
    list_filter = ("categoria", "publicada")
    list_editable = ("publicada",)
    list_per_page = 10
