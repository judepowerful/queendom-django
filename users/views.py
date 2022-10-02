import json
from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from users.forms import RegistrationForm, AuthenticationForm
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string 
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from .tokens import account_activation_token

from django.views import View
from django.http import HttpResponse
from django.core.mail import EmailMessage  
from users.models import Account
from django.contrib.auth import get_user_model

def test(request):
    return render(request, 'users/email_verified.html')

def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():

            account = form.save(commit=False)
            account.is_active = False
            account.save()
            # input information
            email = form.cleaned_data.get('email')
            full_name = form.cleaned_data.get('full_name')
            raw_password = form.cleaned_data.get('password1')
            # ---
            current_site = get_current_site(request)
            
            # login the account
            # account = authenticate(email=email, password = raw_password)
            
            message = render_to_string('users/email_to_verify.html', {  
                'fullname': full_name,  
                'domain': current_site.domain,  
                'uid':urlsafe_base64_encode(force_bytes(account.pk)),  
                'token':account_activation_token.make_token(account),  
            })  
            email_message = EmailMessage(  
                        "Activate your account on Queendom!", message, to=[email]  
            )  
            email_message.send()

            # message to verify account
            email_confirmation_message = 'Please confirm your email: ' + email + ' before use.'
            context['email_confirmation_message'] = email_confirmation_message
        else:
            context['registration_form'] = form

            # return errors of input
            for field in form:
                if field.errors:
                    signup_error = field.errors
                    context['signup_error'] = signup_error
                    
    else: # Get request
        form = RegistrationForm()
    context['registration_form'] = form
    return render(request, 'users/sign_up.html', context)



def logout_view(request):
    logout(request)
    return redirect('index')



def login_view(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("index")

    if request.POST:
        form = AuthenticationForm(request.POST)
        email = request.POST['email']
        password = request.POST['password']
        check_if_user_exists = Account.objects.filter(email=email).exists()

        # check if account exists
        if(check_if_user_exists):

            # if so, check password
            user = authenticate(email=email, password=password)
            if (user):
                login(request, user)
                return redirect("index")

            # if password incorrect
            else:
                password_error = "Your password is incorrect."
                context['password_error'] = password_error
        
        # if account does not exists
        else:
            account_error = "No account exists with this email."
            context['account_error'] = account_error
    else:
        form = AuthenticationForm()
    context['login_form'] = form
    return render(request, 'users/sign_in.html', context)




def activate(request, uidb64, token):  
    User = get_user_model()  
    try:  
        uid = force_str(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save()  
        return render(request, 'users/email_verified.html')  
    else:  
        return HttpResponse('Activation link is invalid!')  