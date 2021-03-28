from django.urls import path
from . import api

urlpatterns = [
    path('', api.TaskListView.as_view()),
    path('new/', api.TaskCreateView.as_view()),
    path('<int:pk>/', api.TaskDeleteView.as_view()),
]