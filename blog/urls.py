from django.urls import path
from . import views
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', BlogView.as_view(), name='index'),
    path('like/', views.like, name='like'),
    path('me/', self_profile_view, name="self_profile"),
    path('profile/edit/', edit_profile_view.as_view(), name='edit_profile'),
    path('feedback/', views.add_feedback, name='add_feedback'),
]