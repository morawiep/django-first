from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'kluby', views.KlubViewSet, basename='kluby')
router.register(r'ligi', views.LigaViewSet, basename='ligi')
router.register(r'piłkarze', views.PiłkarzViewSet, basename='piłkarze')
router.register(r'agenci', views.AgentViewSet, basename='agenci')

urlpatterns = [
    path('', include(router.urls))
]