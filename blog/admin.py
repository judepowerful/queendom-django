from django.contrib import admin

from blog.models import BlogPost, Image

admin.site.register(BlogPost)
admin.site.register(Image)
