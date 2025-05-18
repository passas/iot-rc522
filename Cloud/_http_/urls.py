from django.urls import path

from . import views, api

app_name = '_http_'

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views._login, name='login'),
    path('logout', views._logout, name='logout'),
    path('register', views._register, name='register'),
    path('profile', views.profile, name='profile'),
    path('train', views.train, name='train')
]

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns += [
    path('api/health', api.HealthView.as_view(), name='api_health'),
    path('api/health/agent', api.HealthAgent.as_view(), name='api_health_agent'),

    path('api/login', TokenObtainPairView.as_view(), name='api_login'),
    path('api/register', api.Register.as_view(), name='api_register'),

    path('api/client', api.Client.as_view(), name='api_client'),
    path('api/contracts', api.Contracts.as_view(), name='api_contracts'),
    path('api/tickets', api.Tickets.as_view(), name='api_tickets'),
    path('api/sensor', api.Sensor.as_view(), name='api_sensor'),
]