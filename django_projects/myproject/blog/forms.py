#...    
from django import forms
class BlogForm(forms.Form):
    blog_name = forms.CharField(label='Blog Name')  
    blog_tag_line = forms.CharField(label='Blog Tagline')  

	
class SignupForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput())
	email = forms.CharField(widget=forms.TextInput())
	password = forms.CharField( widget=forms.PasswordInput())

class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput())
	password = forms.CharField(widget=forms.PasswordInput())

class UploadFileForm(forms.Form):
	image = forms.FileField( widget=forms.FileInput(),required=False)   

   	