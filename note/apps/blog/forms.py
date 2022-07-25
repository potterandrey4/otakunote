from django import forms
from .models import *

class AddReviewForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'type_title', 'text')
		exclude = ('id_for_user',)