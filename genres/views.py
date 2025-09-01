from django.http import JsonResponse
import json
from genres.models import Genre
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from genres.serializers import GenreSerializer
# Create your views here.


class GenreCreateListView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


# @csrf_exempt
# def genre_view(request):
#     if request.method == 'GET':
#         genres = Genre.objects.all()
#         data = [{'id': genre.id, 'name': genre.name} for genre in genres]
#         return JsonResponse(data, safe=False)

#     elif request.method == 'POST':
#         data = json.loads(request.body.decode('utf-8'))
#         new_genre = Genre(name=data['name'])
#         new_genre.save()
#         return JsonResponse({'id': new_genre.id, 'name': new_genre.name}, status=201)




class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer



# @csrf_exempt
# def genre_detail_view(request, pk):
#     genre = get_object_or_404(Genre, pk=pk)
#     if request.method == 'GET':
#         data = [{'id': genre.id, 'name': genre.name}]
#         return JsonResponse(data, safe=False)
    
#     elif request.method == 'PUT':
#         data = json.loads(request.body.decode('utf-8'))
#         genre.name = data['name']
#         genre.save()
#         return JsonResponse({'id': genre.id, 'name': genre.name}, status=201)

#     elif request.method == 'DELETE':
#         genre.delete()
#         return JsonResponse({'message': 'Excluido com sucesso.'}, status = 204)
    

