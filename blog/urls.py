from django.urls import path
from . import views
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', BlogView.as_view(), name='index'),
    path('like/', views.like, name='like'),

]