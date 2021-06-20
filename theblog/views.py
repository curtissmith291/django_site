from django.shortcuts import render
from django.views.generic import ListView, DetailView
from theblog.models import Post

# Create your views here.

class BlogView(ListView):
    model = Post
    template_name = 'blog.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

