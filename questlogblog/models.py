from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date_of_post = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="blog_likes")
    dislikes = models.ManyToManyField(User, related_name="blog_dislikes")

    def total_likes(self):
        return self.likes.count()

    def total_dislikes(self):
        return self.dislikes.count()

    def __str__(self):
        return self.title + " - " + str(self.author)

    def get_absolute_url(self):
        return reverse("article_details", args=(str(self.id)) )

