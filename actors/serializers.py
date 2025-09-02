from rest_framework import serializers
from actors.models import Actor


class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = '__all__'

    def to_internal_value(self, data):
        data = data.copy()

        if 'nationality' in data and isinstance(data['nationality'], str):
            data['nationality'] = data['nationality'].upper()
        return super().to_internal_value(data)