from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required

from users.models import Account, Profile
from django.http import HttpResponse

# Index view for blog
def blog_view(request):
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

def frontend_view(request):
    return render(request, 'blog/popups/create-post-forum.html')