from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def uniqueusernamevalidator(value):
    if get_user_model().objects.filter(username__exact=value).exists():
        raise ValidationError('User with this username already exists')

def uniqueemailvalidator(value):
    if get_user_model().objects.filter(email__exact=value).exists():
        raise ValidationError('User with this email already exists')

class SignupForm(forms.Form):
    screen_name = forms.CharField(max_length=50,required=True)
    username = forms.CharField(max_length=50,required=True)
    email = forms.EmailField(max_length=50,required=True)
    password = forms.CharField(widget=forms.PasswordInput(),required=True,max_length=20, min_length=6)
    confirmpassword = forms.CharField(widget=forms.PasswordInput(),label="Confirm your password",required=True,max_length=20,min_length=6)
    def __init__(self,*args,**kwargs):
        super(SignupForm, self).__init__(*args,**kwargs)
        self.fields['username'].validators.append(uniqueusernamevalidator)
        self.fields['email'].validators.append(uniqueemailvalidator)
    def clean(self):
        super(SignupForm, self).clean()
        password = self.cleaned_data.get('password')
        confirmpassword = self.cleaned_data.get('confirmpassword')
        if password and password!=confirmpassword:
            self.add_error('password','Passwords do not match')
            self.add_error('confirmpassword','Passwords do not match')

        return self.cleaned_data;
