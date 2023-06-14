from django.urls import path
from .views import *

#Our Urls
# app_name ="app"
urlpatterns = [
    path('', home, name="home"),
    path('all_journals/', all_journals, name="all_journals"),
    path('editorial_board/', editorial_board, name="editorial_board"),
    path('authors_guide_download/', authors_guide_download, name="authors_guide_download"),
    path('download/<int:pk>', download, name="download"),
    path('journal_detail/', journal_detail, name="journal_detail"),
    path('about_page/', about_page, name="about_page"),
    path('contact_message/', contact_message, name="contact_message")
]