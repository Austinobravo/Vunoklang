from django.urls import path
from .views import *

#Our Urls
# app_name ="app"
urlpatterns = [
    path('', home, name="home"),
    path('event_details/', event_details, name="event_details"),
    path('event_listing/', event_listing, name="event_listing"),
    path('editorial_board/', editorial_board, name="editorial_board"),
    path('authors_guide_download/', authors_guide_download, name="authors_guide_download"),
    path('download/<int:pk>', download, name="download"),
    path('journal_detail/', journal_detail, name="journal_detail"),
]