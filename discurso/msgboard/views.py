from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from discurso import constants as CONST
from django.core.mail import send_mail
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import(ListView, 
								DetailView, DeleteView,
								CreateView, UpdateView)

def home(request):
	data = {
		'title': CONST.APP_NAME+' ~ HOME'
	}
	return render(request, 'msgboard/home.html', data)

def about(request):
	data = {
		'title': CONST.APP_NAME+' ~ About'
	}
	return render(request, 'msgboard/about.html', data)

def contact(request):
	data = {
		'title': CONST.APP_NAME+' ~ Contact'
	}
	return render(request, 'msgboard/contact.html', data)

def email(request):
	# print(request.POST)
	from_address = request.POST['email']
	subject = f'{CONST.APP_NAME} contact from {request.POST["name"]}'
	message = request.POST['comments']
	recipient_list = [CONST.ADMIN_EMAIL]
	send_mail( subject, message, from_address, recipient_list )
	return redirect('/')

# class based detail view
class PostDetailView(DetailView):
	model = Post
	
# NOTE: mixins need to be left of the inheritance class (in this case: CreateView)
class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['category', 'title', 'content']
	success_url = '/'
	# override the default form validation and create the necessary association 
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['category', 'title', 'content']
	success_url = '/'
	# override the default form validation and create the necessary association 
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if (self.request.user == post.author):
			return True
		return False

# NOTE: mixins need to be left of the inheritance class (in this case: UpdateView)
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post

	def test_func(self):
		post = self.get_object()
		if (self.request.user == post.author):
			return True
		return False

