from django.urls import path
from . import api

urlpatterns = [
    path('', api.PurchaseListView.as_view()),
    path('new/', api.PurchaseCreateView.as_view()),
    path('<int:pk>/', api.PurchaseDeleteView.as_view()),
]