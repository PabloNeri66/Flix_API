from rest_framework import generics, views, response, status
from movies.models import Movie
from movies.serializers import MovieSerializer
from rest_framework.permissions import IsAuthenticated
from core.permissions import GlobalDefaultPermission
from django.db.models import Count, Avg
from reviews.models import Review


class MovieCreateListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)


class MovieStatsView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()

    def get(self, request):
        # buscar todos os dados
        total_movies = self.queryset.count()
        movies_by_genre = self.queryset.values('genre__name').annotate(
            count=Count('id')
        )
        total_reviews = Review.objects.count()
        average_stars = Review.objects.aggregate(
            avg_stars=Avg('stars'))['avg_stars']

        return response.Response(
            data={
                "total_movies": total_movies,
                "movies_by_genre": movies_by_genre,
                "total_reviews": total_reviews,
                "average_stars": round(average_stars, 1) if average_stars else 0,
            },
            status=status.HTTP_200_OK,
        )
