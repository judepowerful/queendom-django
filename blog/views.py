from email import message
from email.mime import image
from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.decorators import login_required

from users.models import Account, Profile
from blog.models import BlogPost, Image

from django.http import HttpResponse, JsonResponse

from blog.forms import CreateBlogPostForm, FeedbackForm

@login_required(login_url='/login/')
def create_new_post(request):
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


@login_required(login_url='/login/')
def add_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)

            # link to user
            author = Account.objects.filter(email=request.user.email).first()
            feedback.author = author
        
            # create post models
            feedback.save()

        next = request.POST.get('next', '/')
        return redirect(next)



# Index view for blog
class BlogView(View):
    def post(self, request):
        create_new_post(request)
        return redirect(request.path_info)

    def get(self, request):
        context = {}
        all_posts = BlogPost.objects.all().order_by('-data_published')
        context['posts'] = all_posts
        return render(request, 'blog/index.html', context)

class edit_profile_view(View):
    def post(self, request):
        return redirect(request.path_info)

    def get(self, request):
        context = {}
        return render(request, 'blog/edit-profile.html', context)

# Profile pages for each users
# @login_required(login_url='/login/')
class profile_view(View):
    def post(self, request, pk):
        create_new_post(request)
        return redirect(request.path_info)

    def get(self, request, pk):
        context = {}
        user_found = Account.objects.filter(netid=pk).first()
        if (user_found == None):
            return HttpResponse("No matching account", content_type='text/plain')
        else:
            user_posts = BlogPost.objects.filter(author=user_found).order_by('-data_published')
            context['user'] = user_found
            context['user_posts'] = user_posts
            if(user_found == request.user):
                return render(request, 'blog/user-profile.html', context)
            else:
                return HttpResponse("To see other people profile is still working on process", content_type='text/plain')


@login_required(login_url='/login/')
def self_profile_view(request):
    context = {}
    user_netid = request.user.netid
    return redirect("/%s/" % user_netid)

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