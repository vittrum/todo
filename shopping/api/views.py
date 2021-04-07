from rest_framework import viewsets

from .serializers import PurchaseSerializer

from ..models import Purchase


class PurchaseViewSet(viewsets.ModelViewSet):
    serializer_class = PurchaseSerializer
    queryset = Purchase.objects.all()