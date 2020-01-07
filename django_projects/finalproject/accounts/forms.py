from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import mysub
from django.contrib.auth import get_user_model

User = get_user_model()

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=150, help_text='Email')
    phonenumber=forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'email', 'phonenumber', 'password1', 'password2', )

        def save(self, commit=True):
            user = super(SignupForm, self).save(commit=False)
            user.email = self.cleaned_data["email"]
            if commit:
                user.save()
            return user

#class SignupForm(forms.Form):
#	username = forms.CharField(widget=forms.TextInput())
#	email = forms.CharField(required=False,label='Date', widget=forms.TextInput(attrs={'placeholder': 'whitebricks@gmail.com'}))
#	password = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': '********'}))

class LoginForm(forms.Form):
	email = forms.EmailField(max_length=150, help_text='email')
	password = forms.CharField(widget=forms.PasswordInput())

class contactForm(forms.Form):
	"""docstring for contactForm"""
	name = forms.CharField(widget=forms.TextInput())
	email = forms.EmailField(widget=forms.TextInput())
	message = forms.CharField(widget=forms.TextInput())


class pgForm(forms.Form):
    name = forms.CharField(required=False,label='PG Name',widget=forms.TextInput(attrs={'class': 'form-control'}))
    # city = forms.ChoiceField(required=False,label='City' ,widget=forms.RadioSelect(attrs={'class':'list-unstyled'}), choices=Cities)
    district = forms.CharField(required=False,label='District',widget=forms.TextInput(attrs={'class': 'form-control'})) 
    pg_type = forms.CharField(required=False,label='Type of PG',widget=forms.TextInput(attrs={'class': 'form-control'})) 
    time = forms.CharField(required=False,label='Time',widget=forms.TextInput(attrs={'class': 'form-control'})) 
    status = forms.CharField(required=False,label='Status',widget=forms.TextInput(attrs={'class': 'form-control'})) 
    image = forms.FileField(widget=forms.FileInput(),required=False)
