from email import message
from email.mime import image
from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.decorators import login_required

from users.models import Account, Profile
from blog.models import BlogPost, Image

from django.http import HttpResponse, JsonResponse

from blog.forms import CreateBlogPostForm


# Index view for blog
class BlogView(View):
    def post(self, request):
        form = CreateBlogPostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)

            # link to user
            author = Account.objects.filter(email=request.user.email).first()
            post.author = author
            
            # create post models
            post.save()

            # create image models
            images = request.FILES.getlist('images')
            for image in images:
                Image.objects.create(blogpost=post, image=image)

        return redirect('/')

    def get(self, request):
        context = {}
        all_posts = BlogPost.objects.all().order_by('-data_published')
        context['posts'] = all_posts
        return render(request, 'blog/index.html', context)


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

@login_required(login_url='/login/')
def like(request):
    if request.POST.get('action') == 'post':
        result = ''
        id = request.POST.get('postid')
        post = get_object_or_404(BlogPost, id=id)
        user = Account.objects.filter(email=request.user.email).first()
        if post.likes.filter(email=request.user.email).exists():
            post.likes.remove(request.user)
            post.like_count -= 1
            result = post.like_count
            post.save()
        else:
            post.likes.add(request.user)
            post.like_count += 1
            result = post.like_count
            post.save()
        return JsonResponse({'result': result,})

def frontend_view(request):
    return render(request, 'blog/popups/create-post-forum.html')