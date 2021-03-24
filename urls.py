from django.contrib import admin
from django.urls import path
from . import views
from .views import HomeView, ArticleDetailView, AddPostView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('mainpage', views.mainpage, name='mainpage'),

    path('article/<int:pk>', ArticleDetailView.as_view(), name="article_details"),
    path('add_post', AddPostView.as_view(), name="add_post"),
    ]
#path('article/<int:pk>', ArticleDetailView.as_view(), name="article_details"),