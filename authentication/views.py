from rest_framework import status  # this helps us to know HTTP status of our request
from rest_framework.response import Response  # We need this to convert DB query to JSON
from rest_framework.views import APIView
# Not all the models need CRUD, sometimes all we need to do is read
from rest_framework.viewsets import ReadOnlyModelViewSet
# we can allow all the users to see the view
from rest_framework.permissions import AllowAny

from .serializers import AstronautRegistrationSerializer, AstronautLoginSerializer, UserListSerializer, \
    ScientistRegistrationSerializer, ScientistLoginSerializer
from .models import User, Astronaut


class AstronautRegistrationAPIView(APIView):
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


class ScientistAstronautLoginAPIView(APIView):
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
