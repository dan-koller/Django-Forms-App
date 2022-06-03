from django.urls import path
from .views import MainView, RegisterView

urlpatterns = [
    path("", MainView.as_view(), name="main"),
    path("register/", RegisterView.as_view(), name="register")
]
