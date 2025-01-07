from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

#def home(request):
 #   return render(request, "home.html", {})

class HomeView(ListView):
    model = Post 
    template_name = "home.html"

class ArticleDetails(DetailView):
    model = Post
    template_name = "article_details.html"

class NewPost(CreateView):
    model = Post
    template_name = "cratepost.html"
    fields = "__all__"