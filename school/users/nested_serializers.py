from django.core.exceptions import FieldError, MultipleObjectsReturned, ObjectDoesNotExist
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from users.models import User

__all__ = [
    'NestedUserSerializer',
]


class NestedUserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name']

    def to_internal_value(self, data):

        if data is None:
            return None

        if isinstance(data, dict):
            queryset = self.Meta.model.objects
            try:
                return queryset.get(**data)
            except ObjectDoesNotExist:
                raise ValidationError(
                    "Related object not found using the provided attributes: {}".format(data)
                )
            except MultipleObjectsReturned:
                raise ValidationError(
                    "Multiple objects match the provided attributes: {}".format(data)
                )
            except FieldError as e:
                raise ValidationError(e)

        if isinstance(data, int):
            pk = data
        else:
            try:
                pk = int(data)
            except (TypeError, ValueError):
                raise ValidationError(
                    "Related objects must be referenced by numeric ID or by dictionary of attributes. Received an "
                    "unrecognized value: {}".format(data)
                )

        queryset = self.Meta.model.objects
        try:
            return queryset.get(pk=int(data))
        except ObjectDoesNotExist:
            raise ValidationError(
                "Related object not found using the provided numeric ID: {}".format(pk)
            )
