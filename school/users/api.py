from rest_framework import generics, permissions
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from .serializers import LoginSerializer, RegistrationSerializer, UserSerializer


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = Token.objects.create(user=user)

        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": token.key
        })


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token = Token.objects.get(user=user)

        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": token.key
        })


class UserAPI(generics.RetrieveAPIView):
    permission_classes = [
      permissions.IsAuthenticated,
    ]
    serializer_class = UserSerializer

    def get_object(self):

        return self.request.user
