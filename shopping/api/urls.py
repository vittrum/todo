from rest_framework import routers

from shopping.api.views import PurchaseViewSet

router = routers.SimpleRouter()

router.register('purchases', PurchaseViewSet)

