from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from ticketing.models import Movie, Cinema


def movie_list(request):
    # some decisions
    # 1- selecting data
    movies = Movie.objects.all()
    # 2- some code, like authorization or/and...

    # 3- rendering data
    response_text = '\n'.join(
        '{}: {}'. format(i, movie) for i, movie in enumerate(movies, start=1)
    )
    return HttpResponse(response_text)


def cinema_list(request):
    cinemas = Cinema.objects.all()
    response_text = '''
    <!DOCTYPE html>
    <html>
    <head>
    <title> لیست سینماها </title>
    </head>
    <body>
        <h1> فهرست سینماهای کشور </h1>
        <ul>
        {}
        </ul>
    </body>
    </html>
    '''.format(
        '\n'.join('<li>{}</li>'.format(cinema) for cinema in cinemas)
    )
    return HttpResponse(response_text)