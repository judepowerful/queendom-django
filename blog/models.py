from django.db import models

from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver
import uuid

def upload_location(instance, filename, **kwargs):
    file_path = 'blog/{author_netid}/{post_id}/{filename}'.format(
        author_netid = str(instance.blogpost.author.netid),
        post_id = str(instance.blogpost.id),
        filename=filename,
        )
    return file_path

class BlogPost(models.Model):
    title                   = models.CharField(max_length=50, null=True, blank=True)
    body                    = models.TextField(max_length=5000, null=False, blank=False)
    data_published          = models.DateTimeField(auto_now_add=True, verbose_name="data published")
    data_updated            = models.DateTimeField(auto_now_add=True, verbose_name="data updated")
    author                  = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    id                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug                    = models.SlugField(max_length=100, blank=True, unique=True)
    likes                   = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like', default=None, blank=True)
    like_count              = models.BigIntegerField(default='0')

    def __str__(self):
        return str(self.author.netid) + " / " + self.title + " / " + str(self.data_published)

def pre_save_blog_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.author.netid + "-" + instance.title + "-" + str(instance.id))

pre_save.connect(pre_save_blog_post_receiver, sender=BlogPost)

class Image(models.Model):
    blogpost                = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    image                   = models.ImageField(upload_to=upload_location, null=True, blank=True)

    def __str__(self):
        return str(self.blogpost.author.netid) + " / " + self.blogpost.title + " / " + str(self.blogpost.data_published)

class Feedback(models.Model):
    author                  = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    feedback                = models.TextField(max_length=5000, null=False, blank=False)
    share                   = models.BooleanField(null=False, blank=False)
    date                    = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.author.full_name