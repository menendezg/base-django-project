from django.urls import path

from .views import HomePageView, TestPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("test/pet", TestPageView.as_view(), name="test-pet"),
]