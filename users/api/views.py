from rest_framework import views, generics, viewsets

from ..models import Member

from .serializers import UserSerializer


# TODO: create user, show all users in family
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = Member.objects.all()
