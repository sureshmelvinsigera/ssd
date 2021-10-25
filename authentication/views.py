from rest_framework import generics
from rest_framework import viewsets
# this helps us to know HTTP status of our request
from rest_framework import status
# We need this to convert DB query to JSON
from rest_framework.response import Response
from rest_framework.views import APIView
# Not all the models need CRUD, sometimes all we need to do is read
from rest_framework.viewsets import ReadOnlyModelViewSet
# we can allow all the users to see the view
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import \
    AstronautRegistrationSerializer, \
    AstronautLoginSerializer, \
    UserListSerializer, \
    ScientistRegistrationSerializer, \
    ScientistLoginSerializer, \
    AstronautHealthReportSerializer, \
    ScientistViewAstronautHealthReportSerializer
from .models import User, Astronaut, AstronautHealthReport, Scientist
from rest_framework.exceptions import (
    ValidationError, PermissionDenied
)
from django.shortcuts import get_object_or_404


class AstronautRegistrationAPIView(APIView):
    """
    API endpoint for astronaut registration
    """
    # Allow any user (authenticated or not) to hit this endpoint.
    permission_classes = (AllowAny,)
    serializer_class = AstronautRegistrationSerializer

    def post(self, request):
        user = request.data.get('user', {})
        if not user:
            user = {
                "email": request.data.get('email'),
                "username": request.data.get('username'),
                "password": request.data.get('password'),
                "first_name": request.data.get('first_name'),
                "last_name": request.data.get('last_name'),
            }
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AstronautLoginAPIView(APIView):
    """
    API endpoint for astronaut login
    """
    permission_classes = (AllowAny,)
    serializer_class = AstronautLoginSerializer

    def post(self, request):
        user = request.data.get('user', {})
        if not user:
            user = {
                "username": request.data.get('username'),
                "password": request.data.get('password')
            }
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class ScientistRegistrationAPIView(APIView):
    """
    API endpoint for scientist registration
    """
    # Allow any user (authenticated or not) to hit this endpoint.
    permission_classes = (AllowAny,)
    serializer_class = ScientistRegistrationSerializer

    def post(self, request):
        user = request.data.get('user', {})
        if not user:
            user = {
                "email": request.data.get('email'),
                "username": request.data.get('username'),
                "password": request.data.get('password'),
                "first_name": request.data.get('first_name'),
                "last_name": request.data.get('last_name'),
            }
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ScientistLoginAPIView(APIView):
    """
    API endpoint for scientist login
    """
    permission_classes = (AllowAny,)
    serializer_class = ScientistLoginSerializer

    def post(self, request):
        user = request.data.get('user', {})
        if not user:
            user = {
                "username": request.data.get('username'),
                "password": request.data.get('password')
            }
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class AstronautUserListViewSet(ReadOnlyModelViewSet):
    """
    This view set automatically provides `list` and `detail` actions.
    """
    queryset = Astronaut.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserListSerializer


class AstronautHealthReportViewSet(viewsets.ModelViewSet):
    """
    A view set that listing, retrieving astronauts health reports.
    """
    permission_classes = (IsAuthenticated,)

    serializer_class = AstronautHealthReportSerializer

    def get_queryset(self):
        queryset = AstronautHealthReport.objects.all().filter(astronaut=self.request.user)
        return queryset

    def create(self, request, *args, **kwargs):
        """
        Create new health report for current logged in astronaut
        """
        # obtain the data from the API endpoint
        data = request.data
        # assign the current logged in astronaut to the object and
        # create a new astronaut health report object
        astronaut_health_report = AstronautHealthReport.objects.create(
            weight=data['weight'],
            blood_type=data['blood_type'],
            blood_pressure=data['blood_pressure'],
            heart_rate=data['heart_rate'],
            muscle_mass=data['muscle_mass'],
            astronaut=Astronaut.objects.filter(
                username=self.request.user.username).get()
        )
        # save astronaut health report object to DB
        astronaut_health_report.save()
        # serialize the data for JSON output
        serializer = AstronautHealthReportSerializer(astronaut_health_report)
        return Response(serializer.data)


class ScientistViewAstronautHealthReportViewSet(viewsets.ModelViewSet):
    """
    A view set that listing, retrieving and updating astronauts health reports.
    """
    permission_classes = [IsAuthenticated]

    serializer_class = ScientistViewAstronautHealthReportSerializer

    def get_queryset(self):
        queryset = AstronautHealthReport.objects.all().filter(astronaut=self.request.user)
        return queryset
