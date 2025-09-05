from rest_framework import serializers
from movies.models import Movie
from django.db.models import Avg

class MovieSerializer(serializers.ModelSerializer):

    rate = serializers.SerializerMethodField(read_only=True)


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


    def get_rate(self, obj):
        average = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        if average:
            return round(average, 1)
        return None

