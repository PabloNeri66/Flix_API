
from django.contrib import admin
from django.urls import path
from django.http import request, HttpResponse, JsonResponse

#Genres
from genres.views import GenreRetrieveUpdateDestroyView, GenreCreateListView
#Actors
from actors.views import ActorCreateListView, ActorRetrieveUpdateDestroyView



urlpatterns = [
    path('admin/', admin.site.urls),

    path('genres/', GenreCreateListView.as_view(), name ='genre'), #GET ALL
    path('genres/<int:pk>', GenreRetrieveUpdateDestroyView.as_view(), name='genre-detail-view'),

    path('actors/', ActorCreateListView.as_view(), name='actor_create_list'),
    path('actors/<int:pk>', ActorRetrieveUpdateDestroyView.as_view(), name='actor_retrieve_update_destroy'),
]