from django.contrib import admin
from reviews.models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('movie','stars','comment')
    search_fields = ['name', 'stars']

admin.site.register(Review, ReviewAdmin)