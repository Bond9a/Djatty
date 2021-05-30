from django.urls import path
from sign_in import views

urlpatterns = [
    path("", views.home, name="sign_in"),
]