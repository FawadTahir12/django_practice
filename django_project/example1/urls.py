from django.urls import path
from . import views

urlpatterns = [
    path("", views.createUserView.as_view(), name="user_view_create"),
    path("<str:email>/", views.updateUserView.as_view(), name="user_view_update"),
]