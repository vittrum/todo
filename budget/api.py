from rest_framework import generics

from .models import Budget
from .serializers import BudgetSerializer


class BudgetListView(generics.ListAPIView):
    serializer_class = BudgetSerializer
    queryset = Budget.objects.all()


class BudgetCreateView(generics.CreateAPIView):
    serializer_class = BudgetSerializer
    queryset = Budget.objects.all()


class BudgetDeleteView(generics.DestroyAPIView):
    serializer_class = BudgetSerializer
    queryset = Budget.objects.all()