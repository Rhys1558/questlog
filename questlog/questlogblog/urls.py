from django.urls import path
#from . import views
from .views import HomeView, ArticleDetails, NewPost

urlpatterns = [
    #path("", views.home, name="home"),
    path("", HomeView.as_view(), name="home"),
    path("article/<int:pk>", ArticleDetails.as_view(), name="article_details"),
    path("NewPost/", NewPost.as_view(), name="NewPost"),
]

