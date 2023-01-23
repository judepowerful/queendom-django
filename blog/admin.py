from django.contrib import admin

from blog.models import BlogPost, Image, Feedback

admin.site.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("author", "share", "date", "feedback")
