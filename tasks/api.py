from rest_framework import generics

from .serializers import TaskSerializer
from .models import TodoTask


class TaskCreateView(generics.CreateAPIView):
    serializer_class = TaskSerializer
    queryset = TodoTask.objects.all()


class TaskListView(generics.ListAPIView):
    serializer_class = TaskSerializer
    queryset = TodoTask.objects.all()


class TaskDeleteView(generics.DestroyAPIView):
    serializer_class = TaskSerializer
    queryset = TodoTask.objects.all()