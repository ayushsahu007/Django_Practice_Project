from django.urls import path
from .views import ReceipeAPIView , RegisterAPIView , LoginAPIView
from rest_framework_simplejwt.views import TokenRefreshView
"""  comment for defult jwt token
"""
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name="api_register"),
    path("login/", LoginAPIView.as_view(), name="api_login"),

    path("receipes/", ReceipeAPIView.as_view()),
    path("receipes/<int:id>/", ReceipeAPIView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view(),name="token_refresh"),
]