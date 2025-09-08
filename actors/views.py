from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from actors.models import Actor
from actors.serializers import ActorSerializer
from rest_framework.permissions import IsAuthenticated
from core.permissions import GlobalDefaultPermission

class ActorCreateListView(ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes=(IsAuthenticated, GlobalDefaultPermission,)

class ActorRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes=(IsAuthenticated, GlobalDefaultPermission,)

