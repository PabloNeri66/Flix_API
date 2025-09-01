from django.contrib import admin
from genres.models import Genre

# Register your models here.
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ['name']

admin.site.register(Genre, GenreAdmin)