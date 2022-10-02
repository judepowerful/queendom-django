from dataclasses import field
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm

from users.models import Account

# sign up form
class RegistrationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
            
        icons = getattr(self.Meta, 'icons', dict())

        for field_name, field in self.fields.items():
            if(field.label):
                self.fields[field_name].widget.attrs['placeholder'] = field.label

            # add form-control class to all fields
            field.widget.attrs['class'] = 'form-control'
            # set icon attr on field object
            if field_name in icons:
                field.icon = icons[field_name]

    email = forms.EmailField(max_length=60, help_text='Add a valid queens email address', label='Email')

    class Meta:
        model = Account
        fields = ("email", "full_name", "password1", "password2")
        icons = {'email': 'envelope', 'full_name': 'address-book', 'password1': 'lock', 'password2': 'lock' }


# sign in form
class AuthenticationForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
                
            icons = getattr(self.Meta, 'icons', dict())

            for field_name, field in self.fields.items():
                if(field.label):
                    self.fields[field_name].widget.attrs['placeholder'] = field.label

                # add form-control class to all fields
                field.widget.attrs['class'] = 'form-control'
                # set icon attr on field object
                if field_name in icons:
                    field.icon = icons[field_name]

    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'password')
        icons = {'email': 'envelope', 'password': 'lock'}

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if not authenticate(email=email, password=password):
            raise forms.ValidationError("Invalid login")


# password reset form
class UserPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    email = forms.EmailField(label='email', widget=forms.EmailInput(attrs={
        'placeholder': 'email',
        }))

# password reset new form
class UserPasswordResetNewForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    new_password1 = forms.CharField(label='email', widget=forms.PasswordInput(attrs={
        'placeholder': 'New password',
        }))

    new_password2 = forms.CharField(label='email', widget=forms.PasswordInput(attrs={
        'placeholder': 'New password confirmation',
        }))
