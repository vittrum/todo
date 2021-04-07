from rest_framework import routers

from tasks.api.views import TaskViewSet

router = routers.SimpleRouter()

router.register('tasks', TaskViewSet)

urlpatterns = router.urls