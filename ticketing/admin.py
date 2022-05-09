from django.contrib import admin

# Register your models here.
from ticketing.models import Movie, ShowTime, Cinema

admin.site.register(Movie)
admin.site.register(ShowTime)
admin.site.register(Cinema)
