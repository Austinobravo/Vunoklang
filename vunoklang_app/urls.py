from django.urls import path
from .views import *

#Our Urls
# app_name ="app"
urlpatterns = [
    path('', home, name="home"),
<<<<<<< HEAD
    path('all_journals/', all_journals, name="all_journals"),
=======
    path('event_details/', event_details, name="event_details"),
    path('event_listing/', event_listing, name="event_listing"),
>>>>>>> f53b3285715e70b3f774d14b55489e282fd24502
    path('editorial_board/', editorial_board, name="editorial_board"),
    path('authors_guide_download/', authors_guide_download, name="authors_guide_download"),
    path('download/<int:pk>', download, name="download"),
    path('journal_detail/', journal_detail, name="journal_detail"),
<<<<<<< HEAD
=======
    path('event_listing/', event_listing, name="event_listing"),
>>>>>>> f53b3285715e70b3f774d14b55489e282fd24502
    path('about_page/', about_page, name="about_page"),
    path('contact_message/', contact_message, name="contact_message")
]