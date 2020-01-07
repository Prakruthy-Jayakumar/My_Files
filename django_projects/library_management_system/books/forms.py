from django import forms
class BookForm(forms.Form):
	#use_required_attribute = False
    #book_name = forms.CharField(label='Book Name')  
    #book_title = forms.CharField(label='Book Title')  
    #insert_date=forms.CharField(label='Date')
    book_name = forms.CharField(required=False,label='Book Name') 
    book_title = forms.CharField(required=False,label='Book Title') 
    insert_date = forms.CharField(required=False,label='Date', widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}))
class SignupForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput())
	email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'django@gmail.com'}))
	password = forms.CharField( widget=forms.PasswordInput())
class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput())
	password = forms.CharField(widget=forms.PasswordInput())