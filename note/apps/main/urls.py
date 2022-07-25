from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('book/', views.books, name='books'),
    path('book/filter', views.FilterBook.as_view(), name='book_filter'),
    #path('book/book_info/<book_id>', views.BookInfo.as_view(), name = 'book_info'),
    path('book/book_info/<book_id>/', views.book_info, name = 'book_info'),
    path('book/book_info/<book_id>/edit', views.BookEdit.as_view(), name = 'book_edit'),
    path('book/add/', views.AddBook.as_view(), name='add_book'),
    
    path('film/', views.films, name='films'),
    path('film/film_info/<film_id>', views.film_info, name = 'film_info'),
    path('film/film_info/<film_id>/edit', views.FilmEdit.as_view(), name = 'film_edit'),
    path('film/add/', views.AddFilm.as_view(), name='add_film'),
    
    path('serial/', views.serials, name='serials'),
    path('serial/serial_info/<serial_id>', views.serial_info, name = 'serial_info'),
    path('serial/serial_info/<serial_id>/edit', views.SerialEdit.as_view(), name = 'serial_edit'),
    path('serial/add/', views.AddSerial.as_view(), name='add_serial'),
    
    path('contact/', views.reviews, name='reviews')
]
