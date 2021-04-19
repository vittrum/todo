from rest_framework import viewsets

from .serializers import TaskSerializer

from ..models import TodoTask


# TODO: assign task to a user in family
# TODO: show all tasks of a user
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = TodoTask.objects.all()