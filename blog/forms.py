from django import forms

from blog.models import BlogPost, Image

class CreateBlogPostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ['title', 'body']

class UploadImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ['image',]