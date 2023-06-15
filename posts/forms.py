from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *
from django.contrib.auth.models import User

from captcha.fields import CaptchaField, CaptchaTextInput


class RegisterUserForm(UserCreationForm):
    captcha = CaptchaField(label='Are you human?', widget = CaptchaTextInput(attrs={'class':'captcha'}))
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'captcha')
        widgets = {'username': forms.TextInput(attrs={'class':'form-input'}),
                   'password1': forms.PasswordInput(attrs={'class':'form-input'}),
                   'password2': forms.PasswordInput(attrs={'class':'form-input'}),
                   'email':forms.EmailInput(attrs={'class':'form-input'})
        }



class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='username', widget = forms.TextInput(attrs={'class':'form-input'}))
    password = forms.CharField(label='password', widget = forms.PasswordInput(attrs={'class':'form-input'}))
    captcha = CaptchaField(label='Are you human?', widget = CaptchaTextInput(attrs={'class':'captcha'}))


class AddNewForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.fields['category'].empty_label = 'choose one'
        self.fields['slug'].label = 'URL'

    class Meta:
        model = Content
        fields = ['title', 'text_of_content', 'picture_of_content', 'is_published', 'slug',  'category']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-input'}),
            'text_of_content': forms.Textarea(attrs={'cols':60, 'rows':10, 'class':'form-input'}),
            'picture_of_content' : forms.FileInput(attrs={'class':'form-input'}),
            'is_published' : forms.CheckboxInput(attrs={'class':'form-input-checkbox'}),
            'slug': forms.TextInput(attrs={'class':'form-input'}),
            'category' : forms.Select(attrs={'class':'form-input-select'}),
        
        }
    
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('too long')
        
        return title


    