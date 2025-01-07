from django.urls import path
#from . import views
from .views import HomeView, ArticleDetails, NewPost, EditPost

urlpatterns = [
    #path("", views.home, name="home"),
    path("", HomeView.as_view(), name="home"),
    path("article/<int:pk>", ArticleDetails.as_view(), name="article_details"),
    path("NewPost/", NewPost.as_view(), name="NewPost"),
    path("article/editpost/<int:pk>", EditPost.as_view(), name="edit_post"),
]

