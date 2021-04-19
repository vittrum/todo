from rest_framework import viewsets

from ..models import Budget

from .serializers import BudgetSerializer


# todo: show budget lef
# todo: show budget overall
# todo: setup budget for date
class BudgetViewSet(viewsets.ModelViewSet):
    serializer_class = BudgetSerializer
    queryset = Budget.objects.all()
