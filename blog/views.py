from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required

from users.models import Account, Profile

def blog_view(request):
    return render(request, 'blog/index.html')

@login_required(login_url='/login/')
def profile_view(request, pk):
    context = {}
    user_object = Account.objects.get(netid=pk)

    return render(request, 'blog/user-profile.html', {})