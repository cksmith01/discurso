from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# reference: https://docs.djangoproject.com/en/2.2/ref/models/fields/

class Post(models.Model):
	title = models.CharField(max_length=250)
	category = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	date_updated = models.DateTimeField(default=timezone.now)
	votes_up = models.IntegerField()
	votes_down = models.IntegerField()
	edit_count = models.IntegerField()	  # how many times it's been edited
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	archived = models.BooleanField()
	censored = models.BooleanField()	  # flag to indicate this will not be displayed
	root_post_id = models.IntegerField()  # a ref to the original post
	parent_id = models.IntegerField()	  # post they are replying to
	indent = models.IntegerField()		  # how many indents (partent + 1)

	def __str__(self):
		return f'{self.id} {self.title} {self.author.username}'

class PostVote(models.Model):
	post_id = models.IntegerField()		# reference to the Post object
	user_name = models.TextField()		# user name
	user_id	= models.IntegerField()		# reference to the author 
	up_or_down = models.CharField(max_length=1) # U = up, D = down

	def __str__(self):
		return f'{self.id} {self.user_name} {self.up_or_down}'
