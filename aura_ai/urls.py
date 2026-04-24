"""URL configuration for Aura AI backend."""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework import routers

from users.views import (
    RegisterView, LoginView, UserDetailView, LogoutView
)
from authentication.views import (
    DashboardStatsView, AgentListView, AgentDetailView
)
from django.http import views

router = routers.DefaultRouter()
router.register(r'auth/register', RegisterView, basename='auth')
router.register(r'auth/login', LoginView, basename='auth')
router.register(r'auth/refresh', TokenRefreshView, basename='auth')
router.register(r'auth/logout', LogoutView, basename='auth')

router.register(r'dashboard/stats', DashboardStatsView, basename='dashboard')
router.register(r'agents', AgentListView, basename='dashboard')
router.register(r'agents/(?P<id>[^/.]+)', AgentDetailView, basename='dashboard')

app_name = "aura_ai"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include([
        path('auth/', include('users.urls')),
        path('dashboard/', include('authentication.urls')),
    ])),
    path('api/v1/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', views.home, name='home'),
]
