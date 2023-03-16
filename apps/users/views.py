import jwt

from django.conf import settings
from django.core.mail import send_mail

from rest_framework import (
    views, 
    generics, 
    status, 
    permissions
    )
from rest_framework.response import Response
from rest_framework.permissions import (
    AllowAny, 
    IsAuthenticated, 
    IsAdminUser,
    IsAuthenticatedOrReadOnly

    )

from .serializers import (
    RegistrationSerializer, 
    AuthSerializer, ProfileSerializer)
from .models import User




class RegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny ,]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        headers = self.get_success_headers(serializer.data)
        user_payload = {
            'user_id': user.id,
            'username': user.username
        }
        tokens = {
            'access_token': jwt.encode(user_payload, settings.SECRET_KEY, algorithm="HS256"),
            'refresh_token': jwt.encode(user_payload, settings.SECRET_KEY, algorithm="HS256")
        }
        return Response(
            tokens,
            status=status.HTTP_201_CREATED,
            headers=headers
        )
    

class AuthView(generics.GenericAPIView):
    serializer_class = AuthSerializer
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)




class ProfileCreateView(generics.CreateAPIView):
    """Создание профиля"""
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)


class ProfileListView(generics.ListAPIView):
    """Получение списка профилей"""
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAdminUser, IsAuthenticated,)


class ProfileRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """Получение, обновление и удаление профиля"""
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAdminUser, IsAuthenticated,)
