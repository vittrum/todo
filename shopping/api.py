from rest_framework import generics

from .models import Purchase
from .serializers import PurchaseSerializer


class PurchaseListView(generics.ListAPIView):
    serializer_class = PurchaseSerializer
    queryset = Purchase.objects.all()


class PurchaseCreateView(generics.CreateAPIView):
    serializer_class = PurchaseSerializer
    queryset = Purchase.objects.all()


class PurchaseDeleteView(generics.DestroyAPIView):
    serializer_class = PurchaseSerializer
    queryset = Purchase.objects.all()