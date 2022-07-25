from django.db import models
from users.models import User

class GenreBook(models.Model):
	name = models.CharField(max_length=30, verbose_name='Жанр')

	class Meta:
		verbose_name = 'Жанр книги'
		verbose_name_plural = 'Жанры книги'

	def __str__(self):
		return self.name


class GenreFilm(models.Model):
	name = models.CharField(max_length=30, verbose_name='Жанр')

	class Meta:
		verbose_name = 'Жанр фильма'
		verbose_name_plural = 'Жанры фильма'

	def __str__(self):
		return self.name


class Book(models.Model):
	id_for_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	author = models.CharField(max_length=100, verbose_name='Автор')
	title = models.CharField(max_length=100, verbose_name='Название')
	link = models.TextField(verbose_name='Ссылка')
	lastpage = models.IntegerField(verbose_name='Cтраница')
	genre_book = models.ManyToManyField(GenreBook, help_text="Select a genre for this book", verbose_name='Жанры')
	created_date = models.DateTimeField()

	EMOTIONAL_HEAVINESS = [
		('Флафф', 'Флафф'),
		('Нейтрально', 'Нейтрально'),
		('Стекло', 'Стекло'),
	]

	emotional_heaviness = models.CharField(max_length=10, choices=EMOTIONAL_HEAVINESS, default='Нейтрально')

	STATUS_VARIABLE = [
		('Планирую', 'Планирую'),
		('Читаю', 'Читаю'),
		('Прочитано', 'Прочитано'),
		('Заброшено', 'Заброшено')
	]

	status = models.CharField(max_length=10, choices=STATUS_VARIABLE, default='Планирую')

	TYPE_VARIABLE = [
		('Книга', 'Книга'),
		('Фанфик', 'Фанфик'),
		('Манга', 'Манга'),
		('Манхва', 'Манхва'),
		('Комикс', 'Комикс'),
	]

	type_book = models.CharField(max_length=10, choices=TYPE_VARIABLE, default='Книга')


	class Meta:
		ordering = ['-created_date']
		verbose_name = "Книга"
		verbose_name_plural = "Книги"
	

	def __str__(self):
		return self.title


class Film(models.Model):
	id_for_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	title = models.CharField(max_length=50, verbose_name='Название')
	genre_film = models.ManyToManyField(GenreFilm, help_text="Select a genre for this film", verbose_name='Жанры')

	STATUS_VARIABLE = [
		('Планирую', 'Планирую'),
		('Смотрю', 'Смотрю'),
		('Просмотрено', 'Просмотрено'),
		('Заброшено', 'Заброшено')
	]

	status = models.CharField(max_length=11, choices=STATUS_VARIABLE, default='Планирую')

	EMOTIONAL_HEAVINESS = [
		('Флафф', 'Флафф'),
		('Нейтрально', 'Нейтрально'),
		('Стекло', 'Стекло'),
	]
	
	emotional_heaviness = models.CharField(max_length=10, choices=EMOTIONAL_HEAVINESS, default='Нейтрально')

	COUNTRY_VARIABLE = [
		('Другое', 'Другое'),
		('Южная Корея', 'Южная Корея'),
		('Япония', 'Япония'),
		('Китай', 'Китай'),
		('США', 'США'),
		('Россия', 'Россия'),	]

	country_film = models.CharField(max_length=11, choices=COUNTRY_VARIABLE, default='Не выбрано')

	TYPE_VARIABLE = [
		('Фильм', 'Фильм'),
		('Аниме', 'Аниме'),
		('Мульт', 'Мульт')
	]

	type_film = models.CharField(max_length=11, choices=TYPE_VARIABLE, default='Не выбрано')

	link = models.TextField(verbose_name='Ссылка')
	created_date = models.DateTimeField()

	class Meta:
		ordering = ['-created_date']
		verbose_name = 'Фильм'
		verbose_name_plural = 'Фильмы'

	def __str__(self):
		return self.title


class Serial(models.Model):
	id_for_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	title = models.CharField(max_length=50, verbose_name='Название')
	genre_film = models.ManyToManyField(GenreFilm, help_text="Select a genre for this film", verbose_name='Жанры')

	STATUS_VARIABLE = [
		('Планирую', 'Планирую'),
		('Смотрю', 'Смотрю'),
		('Просмотрено', 'Просмотрено'),
		('Заброшено', 'Заброшено')
	]

	status = models.CharField(max_length=11, choices=STATUS_VARIABLE, default='Планирую')

	EMOTIONAL_HEAVINESS = [
		('Флафф', 'Флафф'),
		('Нейтрально', 'Нейтрально'),
		('Стекло', 'Стекло'),
	]
	
	emotional_heaviness = models.CharField(max_length=10, choices=EMOTIONAL_HEAVINESS, default='Нейтрально')

	COUNTRY_VARIABLE = [
		('Другое', 'Другое'),
		('Южная Корея', 'Южная Корея'),
		('Япония', 'Япония'),
		('Китай', 'Китай'),
		('США', 'США'),
		('Россия', 'Россия'),	]

	country_serial = models.CharField(max_length=11, choices=COUNTRY_VARIABLE, default='Не выбрано')

	TYPE_VARIABLE = [
		('Сериал', 'Сериал'),
		('Аниме', 'Аниме'),
		('Мульт', 'Мульт')
	]

	type_serial = models.CharField(max_length=11, choices=TYPE_VARIABLE, default='Не выбрано')

	link = models.TextField(verbose_name='Ссылка')
	last_serie = models.IntegerField(verbose_name='Последняя серия', default=1)
	created_date = models.DateTimeField()


	class Meta:
		ordering = ['-created_date']
		verbose_name = 'Сериал'
		verbose_name_plural = 'Сериалы'

	def __str__(self):
		return self.title

