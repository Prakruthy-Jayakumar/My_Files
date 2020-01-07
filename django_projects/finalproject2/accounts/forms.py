from django import forms

class SignupForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput())
	email = forms.CharField(required=False,label='Date', widget=forms.TextInput(attrs={'placeholder': 'whitebricks@gmail.com'}))
	password = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': '********'}))

class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput())
	password = forms.CharField(widget=forms.PasswordInput())

class contactForm(forms.Form):
	"""docstring for contactForm"""
	name = forms.CharField(widget=forms.TextInput())
	email = forms.CharField(required=False,label='Date', widget=forms.TextInput(attrs={'placeholder': 'whitebricks@gmail.com'}))
	message = forms.CharField(widget=forms.TextInput())


class pgForm(forms.Form):
    name = forms.CharField(required=False,label='pg Name') 
    place = forms.CharField(required=False,label='place') 
    contact = forms.CharField(required=False,label='Contacts')
    Owner=forms.CharField(required=False,label='Owner')

class UploadFileForm(forms.Form):
	image = forms.FileField( widget=forms.FileInput(),required=False)   

