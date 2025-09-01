from django.contrib import admin
from actors.models import Actor


class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthday', 'nationality')
    search_fields = ['name']

admin.site.register(Actor, ActorAdmin)