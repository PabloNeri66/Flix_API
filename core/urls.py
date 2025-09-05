from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Auth
    path('api/v1/', include('authentication.urls')),
    # Genre
    path('api/v1/', include('genres.urls')),
    # Actors
    path('api/v1/', include('actors.urls')),
    # Movies
    path('api/v1/', include('movies.urls')),
    # Reviews
    path('api/v1/', include('reviews.urls')),
]
