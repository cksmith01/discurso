from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='msgboard-home'),
    # path('/', views.home, name='msgboard-home'),
    path('about/', views.about, name='msgboard-about'),
    path('contact/', views.contact, name='msgboard-contact'),
    path('contact/send', views.email, name='msgboard-contact-send'),
    path('post/new', views.PostCreateView, name='msgboard-post-create'),
    path('post/save', views.PostUpdateView, name='msgboard-post-save'),
    path('post/delete', views.PostDeleteView, name='msgboard-post-delete'),
]
