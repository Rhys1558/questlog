from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import Forms, EditForms

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

class EditPost(UpdateView):
    model = Post
    form_class = EditForms
    template_name = "edit_post.html"
    #fields = ["title", "body"]