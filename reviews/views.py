from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from reviews.models import Review
from reviews.serializers import ReviewSerializer
from rest_framework.permissions import IsAuthenticated
from core.permissions import GlobalDefaultPermission


class ReviewListCreateView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes=(IsAuthenticated, GlobalDefaultPermission,)


class ReviewRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes=(IsAuthenticated, GlobalDefaultPermission,)
