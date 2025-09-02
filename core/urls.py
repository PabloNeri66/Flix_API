
from django.contrib import admin
from django.urls import path
from django.http import request, HttpResponse, JsonResponse

#Genres
from genres.views import GenreRetrieveUpdateDestroyView, GenreCreateListView
#Actors
from actors.views import ActorCreateListView, ActorRetrieveUpdateDestroyView
#Movies
from movies.views import MovieCreateListView, MovieRetrieveUpdateDestroyView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('genres/', GenreCreateListView.as_view(), name ='genre'),
    path('genres/<int:pk>', GenreRetrieveUpdateDestroyView.as_view(), name='genre-detail-view'),

    path('actors/', ActorCreateListView.as_view(), name='actor_create_list'),
    path('actors/<int:pk>', ActorRetrieveUpdateDestroyView.as_view(), name='actor_retrieve_update_destroy'),

    path('movies/', MovieCreateListView.as_view(), name = 'movies_list_create'),
    path('movies/<int:pk>', MovieRetrieveUpdateDestroyView.as_view(), name='movies_retrieve_update_delete'),
]