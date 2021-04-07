from rest_framework import views,generics, viewsets

from ..models import User, Family

from .serializers import UserSerializer, FamilySerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class FamilyViewSet(viewsets.ModelViewSet):
    serializer_class = FamilySerializer
    queryset = Family.objects.all()

