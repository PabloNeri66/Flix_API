from django.contrib import admin
from movies.models import Movie


class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'genre', 'release_date', 'resume_short')
    search_fields = ['name', 'genre']
    
    def resume_short(self, obj):
        """LIMITAR A QUANTIDADE DO RESUMO NO TEMPLATE DO ADMIN"""
        max_chars = 100
        if obj.resume and len(obj.resume) > max_chars:
            return obj.resume[:max_chars] + '...'
        return obj.resume or ''


admin.site.register(Movie, MovieAdmin)
