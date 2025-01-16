from django.urls import path
from .views import HomeView, ArticleDetails, NewPost, EditPost, DeletePost, Likes, Dislikes
from django.views.generic import TemplateView
from django.views.defaults import page_not_found, server_error
from django.conf.urls import handler400, handler403, handler404, handler500


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("article/<int:pk>", ArticleDetails.as_view(), name="article_details"),
    path("NewPost/", NewPost.as_view(), name="NewPost"),
    path("article/editpost/<int:pk>", EditPost.as_view(), name="edit_post"),
    path("article/<int:pk>/deletepost", DeletePost.as_view(), name="delete_post"),
    path("like/<int:pk>", Likes, name="like_post"),
    path("dislike/<int:pk>", Dislikes, name="dislike_post"),
]

handler400 = "questlogblog.views.handler400"
handler403 = "questlogblog.views.handler403"
handler404 = "questlogblog.views.handler404"
handler500 = "questlogblog.views.handler500"