from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import PostForm


# Create your views here.
# def home(request):
# return render(request, 'home.html', {})
def mainpage(request):
    return render(request, 'mainpage.html')


class HomeView(ListView):
    model = Post
    template_name = 'home.html'


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'


# class UpdatePost(UpdateView):
def add_post(response):
    if response.method == "POST":
        form = PostForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect('')
    else:
        form = PostForm

    return render(response, 'add_post.html', {'form': form})
