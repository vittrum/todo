from django.urls import path
from . import api

urlpatterns = [
    path('', api.BudgetListView.as_view()),
    path('new/', api.BudgetCreateView.as_view()),
    path('<int:pk>', api.BudgetDeleteView.as_view())
]