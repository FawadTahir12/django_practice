from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("", views.createUserView.as_view(), name="user_view_create"),
    path("<str:email>/", views.updateUserView.as_view(), name="user_view_update"),
    path("login", views.LoginView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("authors/<int:user_id>/", views.AuthorUpdateView.as_view(), name="author-update"),
    path("celery-testing", views.CeleryTesting.as_view(), name="celery-testing")
]