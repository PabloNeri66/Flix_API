from rest_framework import generics
from movies.models import Movie
from movies.serializers import MovieSerializer
from rest_framework.permissions import IsAuthenticated
from core.permissions import GlobalDefaultPermission

class MovieCreateListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes=(IsAuthenticated, GlobalDefaultPermission)


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes=(IsAuthenticated, GlobalDefaultPermission)
