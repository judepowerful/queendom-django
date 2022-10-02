from django.shortcuts import render
from django.views import View

def blog_view(request):
    return render(request, 'blog/index.html')
