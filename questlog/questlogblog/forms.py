from django import forms
from .models import Post

class Forms(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "body", "author")
        # bootstraps form control css style
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Title"}),
            "body": forms.Textarea(attrs={"class": "form-control", "placeholder": "Your Blog"}),
            "author": forms.Select(attrs={"class": "form-control"}),
        }