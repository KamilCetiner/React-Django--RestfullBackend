from django.urls import path
from .views import register_view, profile_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('profile/', profile_view, name="profile")
]
                             