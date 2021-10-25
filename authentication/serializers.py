from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import User, AstronautHealthReport
from .models import Astronaut
from .models import Scientist


class AstronautRegistrationSerializer(serializers.ModelSerializer):
    """Serializers registration requests and creates a new astronaut."""

    password = serializers.CharField(
        # A minimum password length of 8 characters is suggested as a minimum, while a maximum password length of 64 characters is suggested because
        # higher password lengths can be used to perform a denial-of-service due to the increase in hashing computation necessary (OWASP, 2021).
        max_length=64,
        min_length=8,
        write_only=True
    )
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        # List all of the fields that could possibly be included in a request
        # or response
        fields = ('username', 'email', 'first_name',
                  'last_name', 'password', 'token')

    def create(self, validated_data):
        return Astronaut.objects.create_user(**validated_data)


class AstronautLoginSerializer(serializers.ModelSerializer):
    """Serializer login requests and sign in astronaut user"""
    # Configuring read/write modes creates a mutally exclusive scenario- if read_only is set, the value
    # cannot be overwritten, and if write_only is set, the value cannot be read, which improves application security.
    # As an example, password is write_only, so it can be changed, but cannot be read.
    email = serializers.CharField(max_length=255, read_only=True)
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = Astronaut
        fields = ('username', 'email', 'password', 'token')

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)

        # Raise an exception if a
        # username is not provided.
        if username is None:
            raise serializers.ValidationError(
                'A username is required to login'
            )
        # Raise an exception if a
        # password is not provided.
        if password is None:
            raise serializers.ValidationError(
                'A password is required to login'
            )
        # Django handles the process of authentication.
        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with that username or password was not found'
            )
        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated'
            )
        return {
            "username": user.username,
            "email": user.email,
            "token": user.token
        }


class ScientistRegistrationSerializer(serializers.ModelSerializer):
    """Serializers registration requests and creates a scientist user."""

    password = serializers.CharField(
        max_length=255,
        min_length=8,
        write_only=True
    )
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = Scientist
        # List all of the fields that could possibly be included in a request
        # or response
        fields = ('username', 'email', 'first_name',
                  'last_name', 'password', 'token')

    def create(self, validated_data):
        return Scientist.objects.create_user(**validated_data)


class ScientistLoginSerializer(serializers.ModelSerializer):
    """Serializer login requests and sign in astronaut user"""
    # Configuring read/write modes creates a mutally exclusive scenario- if read_only is set, the value
    # cannot be overwritten, and if write_only is set, the value cannot be read, which improves application security.
    # As an example, password is write_only, so it can be changed, but cannot be read.
    email = serializers.CharField(max_length=255, read_only=True)
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = Scientist
        fields = ('username', 'email', 'password', 'token')

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)

        # Raise an exception if a
        # username is not provided.
        if username is None:
            raise serializers.ValidationError(
                'A username is required to login'
            )
        # Raise an exception if a
        # password is not provided.
        if password is None:
            raise serializers.ValidationError(
                'A password is required to login'
            )
        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with that username or password was not found'
            )
        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated'
            )
        return {
            "username": user.username,
            "email": user.email,
            "token": user.token
        }


class UserListSerializer(serializers.ModelSerializer):
    """
    Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes
    that can then be easily rendered into JSON, XML or other content types.
    Serializers also provide deserialization, allowing parsed data to be converted back into complex types,
    after first validating the incoming data.
    Here we Serialize User all the fields from the user model, expect the password
    """

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email'
        )


class AstronautHealthReportSerializer(serializers.ModelSerializer):
    """
        Here we Serialize User all the fields from the AstronautHealthReport model

    """

    class Meta:
        model = AstronautHealthReport
        fields = (
            'id',
            'weight',
            'blood_type',
            'blood_pressure',
            'heart_rate',
            'feedback'
        )


class ScientistViewAstronautHealthReportSerializer(serializers.ModelSerializer):
    """
            Here we Serialize User all the fields from the AstronautHealthReport model, and obtain specific astronaut
            user object. The scientist can perform CRUD operation on the AstronautHealthReport object but not the
            astronaut object it self. Therefore, the serializer field is set to ReadOnlyField
    """
    astronaut = serializers.ReadOnlyField(source='astronaut.username')

    class Meta:
        model = AstronautHealthReport
        fields = (
            'id',
            'astronaut',
            'weight',
            'blood_type',
            'blood_pressure',
            'heart_rate',
            'feedback',
        )
