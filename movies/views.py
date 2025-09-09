from rest_framework import generics, views, response, status
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


class MovieStatsView(views.APIView):
    permission_classes=(IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()

    def get(self, request):
        #buscar todos os dados
        #montar resposta
        #retornar resposta
        return response.Response(
            data={'message':'Funfo'},
            status=status.HTTP_200_OK
        )