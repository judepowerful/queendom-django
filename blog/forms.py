from django import forms
from django.contrib import admin
from blog.models import BlogPost, Image, Feedback


class CreateBlogPostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ['title', 'body']

class UploadImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ['image',]

class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = ['feedback', 'share',]