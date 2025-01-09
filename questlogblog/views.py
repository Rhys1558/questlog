from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import Forms, EditForms
from django.urls import reverse_lazy


class HomeView(ListView):
    model = Post 
    template_name = "home.html"
    ordering = ["-date_of_post"]

class ArticleDetails(DetailView):
    model = Post
    template_name = "article_details.html"

class NewPost(CreateView):
    model = Post
    form_class = Forms
    template_name = "createpost.html"

class EditPost(UpdateView):
    model = Post
    form_class = EditForms
    template_name = "edit_post.html"

class DeletePost(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy("home")