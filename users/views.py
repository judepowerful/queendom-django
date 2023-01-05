import json
from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from users.forms import RegistrationForm, AuthenticationForm, UserPasswordResetForm
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string 
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from .tokens import account_activation_token

from django.views import View
from django.http import HttpResponse
from django.core.mail import EmailMessage, BadHeaderError 
from users.models import Account, Profile
from django.contrib.auth import get_user_model

from django.http import HttpResponse
from django.db.models.query_utils import Q
from django.contrib.auth.tokens import default_token_generator


def test(request):
    return render(request, 'users/password_reset/password_reset_new.html')

def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # input information
            email = form.cleaned_data.get('email')
            full_name = form.cleaned_data.get('full_name')
            raw_password = form.cleaned_data.get('password1')
            # ---
            current_site = get_current_site(request)
            
            account = form.save(commit=False)
            account.is_active = False
            account.netid = email.split('@')[0]
            account.save()

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
            email_message.content_subtype = 'html'
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
    return redirect('blog:index')



def login_view(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("blog:index")

    if request.POST:
        form = AuthenticationForm(request.POST)
        email = request.POST['email']
        password = request.POST['password']

        # retrieve this account
        user_account = Account.objects.filter(email=email).first()
        
        # check if account exists
        if(user_account):
            # if exists, check if account is active
            check_if_user_active = user_account.is_active

            # check password, user will be none if not active
            user = authenticate(email=email, password=password)
            if (user):
                login(request, user)
                return redirect("blog:index")

            # if password incorrect or email not activate
            else:
                if(check_if_user_active):
                    password_error = "Your password is incorrect."
                    context['login_error'] = password_error
                else:
                    email_notactivate_error = "Please confirm your email."
                    context['login_error'] = email_notactivate_error
        
        # if account does not exists
        else:
            account_error = "No account exists with this email."
            context['login_error'] = account_error
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

        # also create new profile for user
        new_profile = Profile.objects.create(user=user)
        new_profile.save()

        return render(request, 'users/email_verified.html')  
    else:  
        return HttpResponse('Activation link is invalid!')

def password_reset_view(request):
    if request.method == 'POST':
        password_form = UserPasswordResetForm(request.POST)
        if  password_form.is_valid():
            data = password_form.cleaned_data['email']
            user_email = Account.objects.filter(Q(email=data))
            current_site = get_current_site(request)
            if user_email.exists():
                for user in user_email:
                    subject = 'Password Reset'
                    email_template_name = 'users/password_reset/password_reset_email.html'
                    parameters = {
                        'fullname': user.full_name,
                        'email': user.email,
                        'domain': current_site.domain,
                        'site_name': 'Queendom',
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': default_token_generator.make_token(user),
                    }
                    email = render_to_string(email_template_name, parameters)
                    message = EmailMessage(subject, email, to=[user.email])
                    message.content_subtype = 'html'
                    try:
                        message.send()
                    except:
                        return HttpResponse('Invalid Header')
                    return redirect('password_reset_done')
    else:
        password_form = UserPasswordResetForm()
    context = {
        'password_form': password_form,
    }
    return render(request, 'users/password_reset/password_reset.html', context)
