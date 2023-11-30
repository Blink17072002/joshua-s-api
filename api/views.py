from django.shortcuts import render
from .models import Models
from django.http import JsonResponse
from .serializers import ModelsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def main_view(request):
    # Collect all the models
    if request.method == 'GET':
        models = Models.objects.all()

        # serialize them
        serializer = ModelsSerializer(models, many=True)

        # return jsonresponse
        return Response({"data": serializer.data})
    
    if request.method == 'POST':
        models = ModelsSerializer(data=request.data)

        if models.is_valid():
            models.save()
            return Response(models.data, status=status.HTTP_201_CREATED)
    

@api_view(['GET', 'PUT', 'DELETE'])
def adjust_models_view(request, pk):
    try:
        models = Models.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        model = ModelsSerializer(models)        
        return Response(model.data, status=status.HTTP_302_FOUND)
    elif request.method == 'PUT':
        model = ModelsSerializer(models, data=request.data)
        if model.is_valid():
            model.save()
            return Response(model.data, status=status.HTTP_200_OK)
    else:
        models.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)
