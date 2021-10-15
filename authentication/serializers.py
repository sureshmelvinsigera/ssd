from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import User, AstronautHealthReport, HealthReportFeedBack
from .models import Astronaut
from .models import Scientist


class AstronautRegistrationSerializer(serializers.ModelSerializer):
    """Serializers registration requests and creates a new astronaut."""

    password = serializers.CharField(
        max_length=255,
        min_length=8,
        write_only=True
    )
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        # List all of the fields that could possibly be included in a request
        # or response
        fields = ('username', 'email', 'first_name', 'last_name', 'password', 'token')

    def create(self, validated_data):
        return Astronaut.objects.create_user(**validated_data)


class AstronautLoginSerializer(serializers.ModelSerializer):
    """Serializer login requests and sign in astronaut user"""
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
        fields = ('username', 'email', 'first_name', 'last_name', 'password', 'token')

    def create(self, validated_data):
        return Scientist.objects.create_user(**validated_data)


class ScientistLoginSerializer(serializers.ModelSerializer):
    """Serializer login requests and sign in astronaut user"""
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
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email'
        )


class AstronautHealthReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = AstronautHealthReport
        fields = (
            'id',
            'weight',
            'blood_type',
            'blood_pressure',
            'heart_rate',
        )


class ScientistViewAstronautHealthReportSerializer(serializers.ModelSerializer):
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
        )
