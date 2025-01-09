from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import Forms, EditForms
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

def Likes(request, pk):
    post = get_object_or_404(Post, id=request.POST.get("post_id"))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse("article_details", args=[str(pk)]))

def Dislikes(request, pk):
    post = get_object_or_404(Post, id=request.POST.get("post_id"))
    post.dislikes.add(request.user)
    return HttpResponseRedirect(reverse("article_details", args=[str(pk)]))

class HomeView(ListView):
    model = Post 
    template_name = "home.html"
    ordering = ["-date_of_post"]

class ArticleDetails(DetailView):
    model = Post
    template_name = "article_details.html"

    def get_context_data(self, *args, **kwargs):
        like_pk = get_object_or_404(Post, id=self.kwargs["pk"])
        total_likes = like_pk.total_likes()
        dislike_pk = get_object_or_404(Post, id=self.kwargs["pk"])
        total_dislikes = dislike_pk.total_dislikes()
        context = super().get_context_data(*args, **kwargs)
        context["total_likes"] = total_likes
        context["total_dislikes"] = total_dislikes
        return context  

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