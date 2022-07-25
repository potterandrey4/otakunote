from django.db import models
from users.models import User

class Post(models.Model):
	id_for_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	title = models.CharField(max_length=100, verbose_name='Тайтл')

	TYPE_VARIABLE = [
		('Книга', 'Книга'),
		('Фильм', 'Фильм'),
		('Сериал', 'Сериал'),
		('Аниме', 'Аниме'),
		('Мульт', 'Мульт'),
		('Игра', 'Игра')
	]

	type_title = models.CharField(max_length=11, choices=TYPE_VARIABLE, default='Не выбрано')

	text = models.TextField(verbose_name='Текст реценции')

	class Meta:
		verbose_name = 'Рецензия'
		verbose_name_plural = 'Рецензия'

	def __str__(self):
		return self.title 