from books.models import Books
from django.shortcuts import render
from .forms import BookForm,SignupForm, LoginForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout



def add_books(request):
    if request.method == 'POST':


        x = BookForm(request.POST)

        if x.is_valid():

            book_name_user = x.cleaned_data['book_name'] 
            book_title_user =x.cleaned_data['book_title'] 
            book_date=x.cleaned_data['insert_date']

            book_object = Books(name=book_name_user, title=book_title_user, date=book_date)
            book_object.save() # will save the data from the form to database
                
            return HttpResponseRedirect('listbook')

    else:
        x = BookForm(request.POST)
        return render(request, 'add_book.html', {'form': x})   

def showBookDetails(request,requested_book_id):
    book_details= Books.objects.get(id=requested_book_id) 
    context = {"book_details":book_details}
    return render(request,"view_books.html",context)   


def listBooks(request):
    book_details = Books.objects.all()
    context = {"result":book_details}
    return render(request,"list_details.html",context)   


def editDetails(request,requested_book_id):
    if request.method == 'POST': #method is GET so else part is going to work

        x = BookForm(request.POST)
        if x.is_valid():
            book_details = Books.objects.get(id=requested_book_id)
            # this will select datafrom database 
            book_details.name = x.cleaned_data['book_name']
            book_details.title = x.cleaned_data['book_title']
            book_details.date = x.cleaned_data['insert_date']
            book_details.save()
            return HttpResponseRedirect("/listbook")

                

    else:

        book_details = Books.objects.get(id=requested_book_id) # this will select datafrom database 
        x = BookForm(initial={"book_name":book_details.name,"book_title":book_details.title,"insert_date":book_details.date}) # this will set initial values in the form from selected data

    return render(request, 'editedbook.html', {'form': x,'book_id':requested_book_id,})  

def deleteDetails(request,requested_book_id):

    book_details = Books.objects.get(id=requested_book_id)  
    book_details.delete()
   # return HttpResponse('Deleted successfully')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def signup(request):
    if request.method == 'POST':
            signup_form = SignupForm(request.POST)
            if signup_form.is_valid():
                username = signup_form.cleaned_data['username'] 
                email = signup_form.cleaned_data['email']   
                password = signup_form.cleaned_data['password']

                if  User.objects.filter(username=username).exists():
                    #messages.add_message(request, messages.INFO, "Username/Email Already Exists")
                    #return HttpResponse("Username/Email Already Exists")
                    messages.info(request, 'Username already exists.')
   
                else:   
                
                    user = User.objects.create_user(username, email, password)
                    user.save()
                    current_site = get_current_site(request)
                    mail_subject = 'Activate your blog account.'
                    message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'sign.html', {'form': form})


def loginAction(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('listbook')
        retur
    else:   
        if request.method == 'POST':
            login_form = LoginForm(request.POST)
            if login_form.is_valid():

                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']

                user = authenticate(username=username, password=password)
                            
                if user is not None:
                    if user.is_active:
                        login(request, user)    
                        return HttpResponseRedirect('listbook')
                    else:
                        #return HttpResponse('Your account is not active')
                        messages.warning(request, 'your account is not active')

                else:
                    #return HttpResponse('The Account does not exists')
                    messages.warning(request, 'The account does not exists')

            else:
                login_form = LoginForm()
                return render(request, "login.html",{"form":login_form})
        else:
            login_form = LoginForm()
        return render(request, "login.html",{"form":login_form})



def logout_view(request):
    logout(request)
    return HttpResponseRedirect('signup')
    # Redirect to a success page.ss 
    