from django.shortcuts import render
from django.views import View

# Create your views here.
class Users(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'users/users.html')
