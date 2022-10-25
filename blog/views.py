from multiprocessing import context
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required

from users.models import Account, Profile
from blog.models import BlogPost

from django.http import HttpResponse

from blog.forms import CreateBlogPostForm


# Index view for blog
class BlogView(View):
    def post(self, request):
        form = CreateBlogPostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            obj = form.save(commit=False)
            author = Account.objects.filter(email=request.user.email).first()
            obj.author = author
            obj.save()
        return redirect('/')

    def get(self, request):
        context = {}
        
        
        context['posts'] = BlogPost.objects.all()
        return render(request, 'blog/index.html', context)

# View to create a blog
def create_blog_view(request):
    if request.POST:
        form = CreateBlogPostForm(request.POST or None, request.FILES or None)
        title = request.POST['post_title']
        body = request.POST['post_body']
        if form.is_valid():
            obj = form.save(commit=False)
            author = Account.objects.filter(email=request.user.email).first()
            obj.author = author
            obj.save()
            form = CreateBlogPostForm()

    else:
        return render(request, 'blog/index.html')

# Profile pages for each users
# @login_required(login_url='/login/')
def profile_view(request, pk):
    context = {}
    user_found = Account.objects.filter(netid=pk).first()
    if (user_found == None):
        return HttpResponse("No matching account", content_type='text/plain')
    else:
        return render(request, 'blog/user-profile.html', {})

def post_view(request, user_netid, post_id):
    post = BlogPost.objects.filter(id=post_id).first()
    if (post == None):
        return HttpResponse("No matching post", content_type='text/plain')
    else:
        return render(request, 'blog/user-profile.html', {})

def frontend_view(request):
    return render(request, 'blog/popups/create-post-forum.html')