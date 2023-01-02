from django.contrib.auth.forms import UserCreationForm as DjangoUserCreationForm, AuthenticationForm as DjangoAuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_user_model
from django import forms
from users.utils import send_email_for_verify
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .models import *

STATUS_CHOICES = [
    ('Флафф', 'Флафф'),
    ('Нейтрально', 'Нейтрально'),
    ('Стекло', 'Стекло'),
]



User = get_user_model()

class AuthenticationForm(DjangoAuthenticationForm):

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username is not None and password:
            self.user_cache = authenticate(
                self.request,
                username=username,
                password=password,
            )
            if not self.user_cache.email_verify:
                send_email_for_verify(self.request, self.user_cache)
                raise ValidationError(
                    'Email not verify, check your email',
                    code='invalid_login',
                )

            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data


class UserCreationForm(DjangoUserCreationForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'})
    )

    class Meta(DjangoUserCreationForm.Meta):
        model = User
        fields = ("username", "email")



class RegisterUserForm(UserCreationForm):
	#first_name = forms.CharField(label='first_name', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'first_name'}))
	username = forms.CharField(label='Nickname', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Nickname'}))
	email = forms.EmailField(label='email', widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'email', 'autocomplete': 'email'}))
	password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Пароль'}))
	password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Повторите пароль'}))

	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')



class AddBookForm(forms.ModelForm):
	#status = forms.MultipleChoiceField(label='Статус', required=False, widget=forms.Select(), choices=STATUS_CHOICES)
	link = forms.CharField(label='Ссылка', widget=forms.Textarea(attrs={'class': 'form-input', 'rows': 4}))
	class Meta:
		model = Book
		fields = ('title', 'author', 'type_book', 'genre_book', 'lastpage', 'emotional_heaviness',  'status', 'link')
		exclude = ('id_for_user','created_date',)


class ChangeBookForm(forms.ModelForm):
	class Meta:
		model = Book
		fields = ('lastpage', 'status')
		exclude = ('title', 'author', 'genre_book', 'link', 'emotional_heaviness', 'type_book', 'id_for_user','created_date',)


class AddFilmForm(forms.ModelForm):
	#status = forms.MultipleChoiceField(label='Статус', required=False, widget=forms.Select(), choices=STATUS_CHOICES)
	link = forms.CharField(label='Ссылка', widget=forms.Textarea(attrs={'class': 'form-input', 'rows': 4}))
	class Meta:
		model = Film
		fields = ('title', 'type_film', 'emotional_heaviness', 'country_film', 'genre_film', 'status', 'link')
		exclude = ('id_for_user','created_date',)

class ChangeFilmForm(forms.ModelForm):
	class Meta:
		model = Film
		fields = ('status',)
		exclude = ('title', 'genre_book', 'emotional_heaviness', 'type_film', 'country_film', 'id_for_user','created_date',)


class AddSerialForm(forms.ModelForm):
	link = forms.CharField(label='Ссылка', widget=forms.Textarea(attrs={'class': 'form-input', 'rows': 4}))
	class Meta:
		model = Serial
		fields = ('title', 'type_serial', 'emotional_heaviness', 'country_serial', 'genre_film', 'status', 'last_serie',  'link')
		exclude = ('id_for_user','created_date',)

class ChangeSerialForm(forms.ModelForm):
	class Meta:
		model = Serial
		fields = ('status', 'last_serie')
		exclude = ('title', 'genre_book', 'link', 'emotional_heaviness', 'type_serial', 'country_serial', 'id_for_user','created_date',)


class ContactForm(forms.Form):
	subject = forms.CharField(label='Тема', widget=forms.TextInput(attrs={'class': 'form-input'}))
	content = forms.CharField(label='Текст', widget=forms.Textarea(attrs={'class': 'form-input', 'rows':5}))
	

class FilterBookForm(forms.Form):
	EMOTIONAL_HEAVINESS=[
		('Флафф', 'Флафф'),
		('Нейтрально', 'Нейтрально'),
		('Стекло', 'Стекло'),
        ]
	emotional_heaviness = forms.ChoiceField(choices=EMOTIONAL_HEAVINESS, widget=forms.RadioSelect)

	STATUS_VARIABLE = [
		('Планирую', 'Планирую'),
		('Читаю', 'Читаю'),
		('Прочитано', 'Прочитано'),
		('Заброшено', 'Заброшено')
	]
	status = forms.ChoiceField(choices=STATUS_VARIABLE, widget=forms.RadioSelect)

	TYPE_VARIABLE = [
		('Книга', 'Книга'),
		('Фанфик', 'Фанфик'),
		('Манга', 'Манга'),
		('Манхва', 'Манхва'),
		('Комикс', 'Комикс'),
	]
	type_book = forms.ChoiceField(choices=TYPE_VARIABLE, widget=forms.RadioSelect)



