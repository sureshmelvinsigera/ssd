from django.conf.urls import url
from authentication.views import AstronautRegistrationAPIView, AstronautLoginAPIView, ScientistRegistrationAPIView, \
    ScientistLoginAPIView, AstronautUserListViewSet, AstronautHealthReportViewSet

urlpatterns = [

    url(r'^users/astronaut/register/$',
        AstronautRegistrationAPIView.as_view(), name='astronaut_register'),
    url(r'^users/astronaut/login/$',
        AstronautLoginAPIView.as_view(), name='astronaut_login'),
    url(r'^users/scientist/register/$',
        ScientistRegistrationAPIView.as_view(), name='scientist_register'),
    url(r'^users/scientist/login/$',
        ScientistLoginAPIView.as_view(), name='scientist_login'),
]
