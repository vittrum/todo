from rest_framework import serializers

from ..models import User, Family


class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = '__all__'
