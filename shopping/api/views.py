from rest_framework import viewsets

from .serializers import PurchaseSerializer

from ..models import Purchase


# Todo: assign a purchase to a user
# todo: show all tasks, assigned to user
# todo: do not assign, if a budget for family is lower, than purchase cost
class PurchaseViewSet(viewsets.ModelViewSet):
    serializer_class = PurchaseSerializer
    queryset = Purchase.objects.all()