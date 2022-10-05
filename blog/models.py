from django.db import models

from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver
import uuid

def upload_location(instance, filename, **kwargs):
    file_path = 'blog/{author_full_name}/{post_id}/{filename}'.format(
        author_full_name = str(instance.author.full_name), 
        title=str(instance.title), 
        post_id = instance.id.hex,
        filename=filename,
        )
    return file_path

class BlogPost(models.Model):
    title                   = models.CharField(max_length=50, null=False, blank=False)
    body                    = models.TextField(max_length=5000, null=False, blank=False)
    image                   = models.ImageField(upload_to=upload_location, null=False, blank=False)
    data_published          = models.DateTimeField(auto_now_add=True, verbose_name="data published")
    data_updated            = models.DateTimeField(auto_now_add=True, verbose_name="data updated")
    author                  = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    id                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug                    = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.title

@receiver(post_delete, sender=BlogPost)
def submission_delete(sender, instance, **kwarg):
    instance.image.delete(False)

def pre_save_blog_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.author.full_name + "-" + instance.title + "-" + instance.id.hex)

pre_save.connect(pre_save_blog_post_receiver, sender=BlogPost)