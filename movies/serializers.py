from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie
from actors.serializers import ActorSerializer
from genres.serializers import GenreSerializer


class MovieListDetailSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    genre = GenreSerializer()  # Aninhamento de Serializer
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resume']

    def get_rate(self, obj):
        average = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        if average:
            return round(average, 1)
        return None


class MovieModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

    def validate_release_date(self, value):
        if value.year < 1935:
            raise serializers.ValidationError('A data de lançamento não pode ser anterior a 1935.')
        return value

    def validate_resume(self, value):
        if len(value) > 200:
            raise serializers.ValidationError('Ultrapassou o limite de 200 caracteres.')
        return value
