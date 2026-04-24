"""URL configuration for user authentication."""
from django.urls import path
from .views import (
    register, login_view, logout_view, user_detail
)

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('me/', user_detail, name='user_detail'),
]
