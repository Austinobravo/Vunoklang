from django.urls import path
from .views import home

#Our Urls

urlpatterns = [
    path('', home, name="home"),
]