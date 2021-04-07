from rest_framework import routers

from .views import BudgetViewSet

router = routers.SimpleRouter()

router.register('budget', BudgetViewSet)

