from rest_framework.serializers import ModelSerializer

from users.models import User

__all__ = [
    'NestedUserSerializer',
]


class NestedUserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name']
