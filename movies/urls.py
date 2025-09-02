from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.MovieCreateListView.as_view(), name='movies_list_create'),
    path('movies/<int:pk>/', views.MovieRetrieveUpdateDestroyView.as_view(), name='movies_retrieve_update_destroy'),
]
