from django.shortcuts import render

from itertools import product

from django.forms import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import GeeksModel
from .serializers import TaskSerializer


@api_view(http_method_names=['GET', 'POST'])
def get_tasks(request):
    if request.method == 'GET':
        tasks = GeeksModel.objects.all()
        serializer = TaskSerializer(instance=tasks, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')

        tasks = GeeksModel.objects.create(title=title, description=description)
        return Response(status=status.HTTP_201_CREATED, data=TaskSerializer(tasks).data)


@api_view(['GET', 'PUT', 'DELETE'])
def tasks_detail_api_view(request, id):
    try:
        tasks = GeeksModel.objects.get(id=id)
    except GeeksModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'ERROR': 'Tasks not found'})

    if request.method == 'GET':
        data = TaskSerializer(tasks).data
        return Response(data=data)

    elif request.method == 'PUT':
        title = request.data.get('title', tasks.title)
        description = request.data.get('description', tasks.description)
        completed = request.data.get('completed', tasks.completed)

        tasks.title = title
        tasks.description = description
        tasks.completed = True if completed == 'true' else False
        tasks.save()
        return Response(status=status.HTTP_200_OK, data=TaskSerializer(tasks).data)

    elif request.method == 'DELETE':
        tasks.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
