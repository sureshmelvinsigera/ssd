"""ssd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from authentication.views import AstronautHealthReportViewSet, AstronautUserListViewSet, \
    ScientistViewAstronautHealthReportViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

router = DefaultRouter()
router.register(r'astronaut/health-reports',
                AstronautHealthReportViewSet, basename='astronaut')
router.register(r'scientist/health-reports',
                ScientistViewAstronautHealthReportViewSet, basename='scientist')
router.register(r'astronauts/in-space', AstronautUserListViewSet,
                basename='astronaut_in_space')

schema_view = get_swagger_view(title='Astronaut API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('', include(router.urls)),
    path(r'swagger-docs/', schema_view),
]
