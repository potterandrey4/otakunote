from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='blog'),
	path('add', views.AddReview.as_view(), name='add_post')
]