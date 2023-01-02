from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseNotFound
from django.contrib.auth.models import User
from django.views.generic import CreateView, ListView, View
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.urls import reverse_lazy, reverse
from django.utils.http import urlsafe_base64_decode
from users.utils import send_email_for_verify
from django.conf import settings
from django.core.exceptions import ValidationError
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.template.loader import render_to_string

from .forms import *
from .models import *


User = get_user_model()

@login_required
def index(request):
	#variable_status_serial = request.GET.get('status_film')
	#variable_status_book = request.GET.get('status_book')

	films = Film.objects.filter(status = 'Смотрю', id_for_user_id = request.user)
	books = Book.objects.filter(status = 'Читаю', id_for_user_id = request.user)
	serials = Serial.objects.filter(status = 'Смотрю', id_for_user_id = request.user)


		#raise Http404('Films не найдены :(')

#	num_users=User.objects.count()
#
#	num_visits=request.session.get('num_visits', 0)
#	request.session['num_visits'] = num_visits+1

	return render(request, 'folder/main.html',
		context={
		'books':books,
		'films':films,
		'serials':serials
		}
	)



User = get_user_model()

class MyLoginView(LoginView):
	form_class = AuthenticationForm


class EmailVerify(View):

	def get(self, request, uidb64, token):
		user = self.get_user(uidb64)

		if user is not None and token_generator.check_token(user, token):
			user.email_verify = True
			user.save()
			login(request, user)
			return redirect('index')
		return redirect('invalid_verify')

	@staticmethod
	def get_user(uidb64):
		try:
			# urlsafe_base64_decode() decodes to bytestring
			uid = urlsafe_base64_decode(uidb64).decode()
			user = User.objects.get(pk=uid)
		except (TypeError, ValueError, OverflowError,
				User.DoesNotExist, ValidationError):
			user = None
		return user


class Register(View):
	template_name = 'registration/register.html'

	def get(self, request):
		context = {
			'form': UserCreationForm()
		}
		return render(request, self.template_name, context)

	def post(self, request):
		form = UserCreationForm(request.POST)

		if form.is_valid():
			username = form.cleaned_data.get('username')
			form.instance.first_name = username
			form.save()
			email = form.cleaned_data.get('email')
			password = form.cleaned_data.get('password1')
			user = authenticate(email=email, password=password)
			send_email_for_verify(request, user)
			return redirect('confirm_email')
		context = {
			'form': form
		}
		return render(request, self.template_name, context)




class AddBook(CreateView):
	form_class = AddBookForm
	template_name = 'folder/add_book.html'
	success_url = reverse_lazy('books')

	def form_valid(self, form):
		form.instance.id_for_user = self.request.user
		form.instance.created_date = timezone.now()
		return super().form_valid(form)

class AddFilm(CreateView):
	form_class = AddFilmForm
	template_name = 'folder/add_film.html'
	success_url = reverse_lazy('films')

	def form_valid(self, form):
		form.instance.id_for_user = self.request.user
		form.instance.created_date = timezone.now()
		return super().form_valid(form)


class AddSerial(CreateView):
	form_class = AddSerialForm
	template_name = 'folder/add_serial.html'
	success_url = reverse_lazy('serials')

	def form_valid(self, form):
		form.instance.id_for_user = self.request.user
		form.instance.created_date = timezone.now()
		return super().form_valid(form)


@login_required
def books(request):
	try:
		all_books = Book.objects.filter(id_for_user_id = request.user)
		paginator = Paginator(all_books, 15)
		page_number = request.GET.get('page')
		page_obj = paginator.get_page(page_number)
		genre_book = GenreBook.objects.all()
	except:
		raise Http404('Books не найдены :(')

	return render(request, 'folder/book.html', {'page_obj': page_obj, 'genre_book': genre_book, })

class FilterBook(CreateView):
	form_class = FilterBookForm
	template_name = 'folder/book.html'

	def get(self, request):
		books = []

		genre = request.GET.get('genre_book')
		emotional_heaviness = request.GET.get('emotional')
		status = request.GET.get('status')
		type_book = request.GET.get('type_book')

		print(status)

		books += Book.objects.filter(emotional_heaviness = emotional_heaviness, genre_book = genre, status = status, type_book = type_book)
		#books.filter(genre_book = genre)
		#books.filter(status = status)
		#books.filter(type_book = type_book)

		paginator = Paginator(books, 15)
		page_number = request.GET.get('page')
		page_obj = paginator.get_page(page_number)
		genre_book = GenreBook.objects.all()

		context = {
			'form': FilterBookForm(),
			'page_obj': page_obj,
			'genre_book': genre_book,

		}
		return render(request, self.template_name, context)

	def post(self, request, book_id):
		form = FilterBookForm(request.POST)

		if form.is_valid():
			paginator = Paginator(books, 15)
			page_number = request.GET.get('page')
			page_obj = paginator.get_page(page_number)
			genre_book = GenreBook.objects.all()
		return render(request, 'folder/book.html', {'page_obj': page_obj, 'form':form})


class BookInfo(CreateView):
	form_class = ChangeBookForm
	template_name = 'folder/book_info.html'

	def get(self, request):
		book = Book.objects.get(id = request.book_id)

		context = {
			'form': ChangeBookForm(),
			'book': book,

		}
		return render(request, self.template_name, context)

	def post(self, request, book_id):
		form = ChangeBookForm(request.POST)
		book = Book.objects.get(id = book_id)
		if form.is_valid():
			form.instance.created_date = timezone.now()
			book.book_id = request.GET.get('page')
			form.save()
		return render(request, 'folder/book_info.html', {'book': book, 'book_id': book_id})


@login_required
def book_info(request, book_id):
	try:
		book = Book.objects.get(id = book_id)
		form = ChangeBookForm
		status_variant = ['Планирую', 'Читаю', 'Прочитано', 'Заброшено']
	except:
		raise Http404('Book не найденa :(')

	return render(request, 'folder/book_info.html', {'book': book, 'form': form, 'status_variant':status_variant})

class BookEdit(View):
	def get(self, request, book_id):
		book = Book.objects.get(id = book_id)
		book.lastpage = request.GET.get("lastpage")
		book.status = request.GET.get("status")
		book.save()
		return redirect('book_info', book_id)

@login_required
def films(request):
	try:
		all_books = Film.objects.filter(id_for_user_id = request.user)
		paginator = Paginator(all_books, 15)
		page_number = request.GET.get('page')
		page_obj = paginator.get_page(page_number)
	except:
		raise Http404('Films не найдены :(')

	return render(request, 'folder/film.html', {'page_obj': page_obj})

@login_required
def film_info(request, film_id):
	try:
		film = Film.objects.get(id = film_id)
		form = ChangeFilmForm
		status_variant = ['Планирую', 'Смотрю', 'Просмотрено', 'Заброшено']
	except:
		raise Http404('Фильм не найден')
	return render(request, 'folder/film_info.html', {'film': film, 'form':form, 'status_variant':status_variant})

class FilmEdit(View):
	def get(self, request, film_id):
		film = Film.objects.get(id = film_id)
		film.status = request.GET.get("status")
		film.save()
		return redirect('film_info', film_id)

@login_required
def serials(request):
	try:
		all_serials = Serial.objects.filter(id_for_user_id = request.user)
		paginator = Paginator(all_serials, 15)
		page_number = request.GET.get('page')
		page_obj = paginator.get_page(page_number)
	except:
		raise Http404('Serials не найдены :(')

	return render(request, 'folder/serial.html', {'page_obj': page_obj,})

@login_required
def serial_info(request, serial_id):
	try:
		serial = Serial.objects.get(id = serial_id)
		form = ChangeSerialForm
		status_variant = ['Планирую', 'Смотрю', 'Просмотрено', 'Заброшено']
	except:
		raise Http404('Сериал не найден')
	return render(request, 'folder/serial_info.html', {'serial': serial, 'form':form, 'status_variant':status_variant})

class SerialEdit(View):
	def get(self, request, serial_id):
		serial = Serial.objects.get(id = serial_id)
		serial.status = request.GET.get("status")
		serial.last_serie = request.GET.get("last_serie")
		serial.save()
		return redirect('serial_info', serial_id)

@login_required
def reviews(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			mail = send_mail(
				form.cleaned_data['subject'],
				form.cleaned_data['content'] + '\n\n from: ' + request.user.email,
				'bloknototaku@gmail.com',
				['bloknototaku@gmail.com'],
				fail_silently=False
				)

			if mail:
				messages.success(request, 'Письмо отправлено')
				return redirect('reviews')
			else:
				messages.error(request, 'Ошибка отправки')
	else:
		form = ContactForm()
	return render(request, 'folder/contact.html', {'form':form})


class BookData:
	def get_genre_book(self):
		return GenreBook.objects.all()





