# Generated by Django 4.1.2 on 2022-10-26 07:26

import blog.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('title', models.CharField(max_length=50)),
                ('body', models.TextField(max_length=5000)),
                ('image1', models.ImageField(blank=True, null=True, upload_to=blog.models.upload_location)),
                ('image2', models.ImageField(blank=True, null=True, upload_to=blog.models.upload_location)),
                ('image3', models.ImageField(blank=True, null=True, upload_to=blog.models.upload_location)),
                ('image4', models.ImageField(blank=True, null=True, upload_to=blog.models.upload_location)),
                ('image5', models.ImageField(blank=True, null=True, upload_to=blog.models.upload_location)),
                ('image6', models.ImageField(blank=True, null=True, upload_to=blog.models.upload_location)),
                ('image7', models.ImageField(blank=True, null=True, upload_to=blog.models.upload_location)),
                ('image8', models.ImageField(blank=True, null=True, upload_to=blog.models.upload_location)),
                ('data_published', models.DateTimeField(auto_now_add=True, verbose_name='data published')),
                ('data_updated', models.DateTimeField(auto_now_add=True, verbose_name='data updated')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
