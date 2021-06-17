from django.conf import settings
from django.contrib.auth.password_validation import (
    validate_password,
    get_password_validators
)
from rest_framework import serializers, exceptions
from django.core.exceptions import ValidationError
from .models import User


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password_confirm = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'email', 'password', 'password_confirm']
        extra_kwargs = {'id': {'read_only': True}}

    def is_unique(self, model, **kwargs):
        try:
            model.objects.get(**kwargs)
            return False
        except model.DoesNotExist:
            return True

    def validate(self, data):

        errors = {}

        if not self.is_unique(User, username=data['username']):
            errors['username'] = "Username already taken"

        if not self.is_unique(User, email=data['email']):
            errors['email'] = "E-mail already taken"

        if data['password'] != data['password_confirm']:
            errors['password'] = "Confirmation password did not match"
        else:
            try:
                validate_password(
                    data['password'],
                    password_validators=get_password_validators(settings.AUTH_PASSWORD_VALIDATORS)
                )
            except ValidationError as e:
                errors['password'] = e.messages

        if errors:
            raise exceptions.ValidationError(errors)

        return data

    def create(self, validated_data):
        password = validated_data.pop('password')
        password_confirm = validated_data.pop('password_confirm')

        user = User(**validated_data)
        user.set_password(password)
        user.save()

        return user
