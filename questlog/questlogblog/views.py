from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import Forms

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
    form_class = Forms
    template_name = "cratepost.html"
    #fields = ("title", "body", "author")