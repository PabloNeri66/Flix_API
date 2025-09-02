from . import views
from django.urls import path

urlpatterns = [
    path('actors/', views.ActorCreateListView.as_view(), name='actor_create_list'),
    path('actors/<int:pk>/', views.ActorRetrieveUpdateDestroyView.as_view(), name='actor_retrieve_update_destroy'),
]
