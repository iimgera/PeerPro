from rest_framework import  serializers
from rest_framework_simplejwt.tokens import RefreshToken

from django.db import IntegrityError
from django.contrib.auth import get_user_model

from .models import User

from djoser.serializers import (
    UserCreateSerializer, 
    UserSerializer
    )



class UserTokenSerializer(serializers.ModelSerializer):
    access_token = serializers.CharField()
    refresh_token = serializers.CharField()

    class Meta:
        fields = (
            'access_token',
            'refresh_token',
        )

class RegistrationSerializer(UserCreateSerializer):
    password = serializers.CharField(write_only=True)

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'password')


User = get_user_model()

class AuthSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise serializers.ValidationError('User does not exist.')

        if not user.check_password(password):
            raise serializers.ValidationError('Invalid password.')

        refresh = RefreshToken.for_user(user)

        return {
            'user_id': user.id,
            'refresh_token': str(refresh),
            'access_token': str(refresh.access_token),
        }


class UserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = User
        fields = [
            'id',
            'username', 
            'email',
            'password',
            ]


# class ProfileSerializer(serializers.ModelSerializer):
#     username = serializers.CharField(max_length=150)

#     class Meta:
#         model = User
#         fields = ('id', 'email', 'username', 'first_name', 'last_name', 'department',)


#     def create(self, validated_data):
#         username = validated_data.pop('username')
#         try:
#             user = User.objects.create_user(username=username, password='defaultpassword')
#         except IntegrityError:
#             raise serializers.ValidationError('Username already exists')
#         profile = Profile.objects.create(user=user, **validated_data)
#         return profile