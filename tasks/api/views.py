from rest_framework import viewsets

from .serializers import TaskSerializer

from ..models import TodoTask

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = TodoTask.objects.all()