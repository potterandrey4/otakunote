from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy, reverse
from .forms import *
from .models import *


def index(request):
	reviews = Post.objects.all()
	return render(request, 'folder/blog.html', {'reviews':reviews})



class AddReview(CreateView):
	form_class = AddReviewForm
	template_name = 'folder/add_post.html'
	success_url = reverse_lazy('blog')

	def form_valid(self, form):
		form.instance.id_for_user = self.request.user
		return super().form_valid(form)