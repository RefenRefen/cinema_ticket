from django.urls import path

from ticketing.views import movie_list, cinema_list


urlpatterns = [
    path('movie/list', movie_list),
    path('cinema/list', cinema_list)
]
