from django.http import JsonResponse
from genres.models import Genre
from rest_framework import generics
from genres.serializers import GenreSerializer
from rest_framework.permissions import IsAuthenticated
from core.permissions import GlobalDefaultPermission



class GenreCreateListView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes=(IsAuthenticated, GlobalDefaultPermission,)


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes=(IsAuthenticated, GlobalDefaultPermission,)
