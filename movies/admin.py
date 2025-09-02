from django.contrib import admin
from movies.models import Movie


class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'genre', 'release_date', 'resume')
    search_fields = ['name', 'genre']

admin.site.register(Movie, MovieAdmin)
