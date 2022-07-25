from django.contrib import admin
from .models import Book, GenreBook, GenreFilm, Film, Serial
from users.models import User

admin.site.register(User)
admin.site.register(Book)
admin.site.register(GenreBook)
admin.site.register(GenreFilm)
admin.site.register(Film)
admin.site.register(Serial)
