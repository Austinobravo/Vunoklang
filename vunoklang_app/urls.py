from django.urls import path
from .views import *

#Our Urls

urlpatterns = [
    path('', home, name="home"),
    path('event_details/', event_details, name="event_details"),
    path('event_listing/', event_listing, name="event_listing"),
    path('about_page/', about_page, name="about_page"),
]