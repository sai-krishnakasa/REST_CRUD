from turtle import title
from django.shortcuts import redirect, render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serialize import TaskSerializer
from .models import Task
# Create your views here.

@api_view(['GET'])
def apiOverView(request):
    return Response('okay')

@api_view(['GET'])
def taskList(request):
    tasks=Task.objects.all()
    task_serail=TaskSerializer(tasks,many=True)
    return Response(task_serail.data)


@api_view(['GET'])
def taskDetail(request,pk):
    tasks=Task.objects.get(id=pk)
    task_serail=TaskSerializer(tasks,many=False)
    return Response(task_serail.data)

@api_view(['GET'])
def taskDelete(request,pk):
    tasks=Task.objects.get(id=pk)
    tasks.delete()
    tasks.save()
    return redirect('api-task_list')


@api_view(['POST'])
def taskCreate(request):
    serializer=TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return redirect('api-task_list')


@api_view(['POST'])
def taskUpdate(request,pk):
    task=Task.objects.get(id=pk)
    serializer=TaskSerializer(instance=task,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return redirect('api-task_list')