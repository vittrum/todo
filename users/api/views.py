from rest_framework import views, generics, viewsets

from ..models import User, Family

from .serializers import UserSerializer, FamilySerializer


# TODO: create user, show all users in family
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


# TODO: create family, show family members
class FamilyViewSet(viewsets.ModelViewSet):
    serializer_class = FamilySerializer
    queryset = Family.objects.all()
