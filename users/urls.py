from django.urls import path

from . import views

urlpatterns = [
    path("api/csrf/", views.CSRFView.as_view()),
    path("api/register/", views.RegisterView.as_view()),
    path("api/login/", views.LoginView.as_view()),
    path("api/logout/", views.LogoutView.as_view()),
]
