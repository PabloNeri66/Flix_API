from . import views
from django.urls import path

urlpatterns = [
    path('reviews/', views.ReviewListCreateView.as_view(), name='review_list_create'),
    path('reviews/<int:pk>/', views.ReviewRetrieveUpdateDestroyView.as_view(), name='review_retrieve_update_destroy'),
]
