from django.urls import path
from .views import *

urlpatterns = [
    path("receipes/", receipes, name="receipes"),
    path("delete-receipes/<int:id>/", delete_receipe, name="delete_receipes"),
    path("update-receipe/<int:id>/", update_receipe, name="update_receipe"),
]